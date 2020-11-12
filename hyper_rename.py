import os
import sys
import argparse
import glob

def exception_handler(func):
	def wrapper(*args, **kwargs):
		try:
			func(*args, **kwargs)
		except PermissionError:
			print()
			print("Access Denied: You are Probably in the Same Directory as the one you're trying to rename\nOr A file that you're trying to open, already has an open instance")
		except Exception as e:
			print()
			print(f"FATAL ERROR: {e}")
	return wrapper

@exception_handler
def hyper_renamer(directory, old_name, new_name, ignored_folders=[], ignored_extensions=[], ignored_files=[]):
	ignored_folders = tuple(ignored_folders)
	ignored_extensions = tuple(ignored_extensions)
	ignored_files = tuple(ignored_files)

	folders = []
	for f in os.walk(directory):
		cfld = f[0]
		#if(not cfld.endswith(ignored_folders)):
		# print(cfld, ignored_folders)
		if(not any(xfd in cfld for xfd in ignored_folders)):
			folders.append(cfld)
			files = f[2]
			#Renaming All Files
			for fn in files:
				if(old_name in fn and not fn.endswith(ignored_extensions) and not fn in ignored_files):
					orig_path = os.path.join(cfld, fn)
					new_path = os.path.join(cfld, fn.replace(old_name, new_name))
					os.rename(orig_path, new_path)
					print(f"Renamed File: {orig_path} -> {new_path}")

	folders = reversed(folders)

	#Renaming Folders
	for fd in folders:
		fd = fd.replace("\\", "/")

		iobs = fd.rfind("/")
		pre = fd[:iobs]
		fdn = fd[iobs+1:]

		if(fdn != ''):
			if(old_name in fdn):
				os.rename(os.path.join(f"{pre}/{fdn}"), os.path.join(f"{pre}/{fdn.replace(old_name, new_name)}"))
				print("Renamed Folder:", os.path.join(f"{pre}/{fdn}"), " --> ", os.path.join(f"{pre}/{fdn.replace(old_name, new_name)}"))
				fdn = fdn.replace(old_name, new_name)
		else:
			if(old_name in pre):
				os.rename(os.path.join(f"{pre}"), os.path.join(f"{pre.replace(old_name, new_name)}"))
				print(f"Renamed Root: {pre} -> {pre.replace(old_name, new_name)}")
				pre = pre.replace(old_name, new_name)
				

	directory = directory.replace(old_name, new_name)
	for f in os.walk(directory):
		for file in f[2]:
			if(not file.endswith(ignored_extensions) and file not in ignored_files and not any(xfd in f[0] for xfd in ignored_folders)):
				src = ""
				try:
					with open(os.path.join(f[0], file), "r") as x:
						src = x.read()
					if(old_name in src):
						src = src.replace(old_name, new_name)
						with open(os.path.join(f[0], file), "w") as x:
							x.write(src)
						print(f"Modified {os.path.join(f[0], file)}")
				except UnicodeDecodeError:
					print(f"Unable to Modify {os.path.join(f[0], file)} : UnicodeDecodeError")
				except Exception as e:
					print(f"Unable to Modify {os.path.join(f[0], file)} : {e}")


if(__name__ == '__main__'):
	parser = argparse.ArgumentParser()
	parser.add_argument('directory', help="Directory To Recursively Rename", type= str)
	parser.add_argument('--oldname', '-o', help="Old Name", type= str)
	parser.add_argument('--newname', '-n', help="New Name", type= str)
	parser.add_argument('--ignored_folders', '-ifd', help="Ignored Folders", type= str, default="")
	parser.add_argument('--ignored_extensions', '-ie', help="Ignored Extensions", type= str, default="")
	parser.add_argument('--ignored_files', '-ifl', help="Ignored Files", type= str, default="")

	args = parser.parse_args()
	print("-------- HyperRename v0.1 --------")

	directory = args.directory
	directory = directory.replace("/", "\\") if directory.endswith("/") else directory+"\\" if(not directory.endswith("\\")) else directory
	old_name = args.oldname
	new_name = args.newname
	i_folders = []
	i_ext = []

	i_folders = [] if args.ignored_folders == "" else args.ignored_folders.replace("[", "").replace("]", "").replace(", ", " ").replace(",", " ").split(" ")
	i_ext = [] if args.ignored_extensions == "" else args.ignored_extensions.replace("[", "").replace("]", "").replace(", ", " ").replace(",", " ").split(" ")
	i_files = [] if args.ignored_files == "" else args.ignored_files.replace("[", "").replace("]", "").replace(", ", " ").replace(",", " ").split(" ")

	# print(i_folders, i_ext, i_files)
	hyper_renamer(directory, old_name, new_name, ignored_folders=i_folders, ignored_extensions=i_ext, ignored_files=i_files)

	print("-------------- Done ---------------")