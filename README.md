# HyperRename
 A Python & Bash Script that can be used to rename Files, Folders, and Subfolders and also replace in files (Currently Supports Windows only)
 This is incredibly useful if you want to rename a folder structure that contains a word in multiple sub-branches. This script recursively goes over each and every file directory and edits not only the filename but also foldernames and its subcontents!
 
 ## Simple Example
 Suppose you have a nested Structure with the word Rest appearing multiple times both in filenames, foldernames and inside the individual files like this:
 
 ### Before Running the Script
![before](https://github.com/synapsecode/HyperRename/blob/main/GithubData/1.JPG)

### Command
```cmd
hren -o Rest -n Test
```



### After Running the Script (Rest -> Test)
![before](https://github.com/synapsecode/HyperRename/blob/main/GithubData/2.JPG)

All instances of Rest in your folders, filenames and inside your files has been replaced with Test. This has occured everywhere at the same time! Isnt this awesome?

## Installation (Windows Only)
### 1. Git Clone this Repo to some folder on your PC
### 2. Make sure you have python3 installed on your PC
### 3. Add the directory path to your environment variables and close cmd and re-open it
### 4. now you can type "hren" in your cmd and it should work!

## Commands
### Arguements
   1. -o (or) --oldname -> This is the name that you want to replace
   2. -n (or) --newname -> This is the name name that you want to replace the old name with
   3. -ifl -> This is the ignored Files represented as a string of a list (like "[test.py, x.bat]")
   4. -ie -> This is the ignored extensions represented as a string of a list (like "[.py, .exe, .pyc]")
   5. -ifd -> THis is the ignored Folders represented as a string of a list (like "[venv, node_modules]")
   
### Examples
Hren Works in the particular directory that you call it from.

1. Basic Rename (Converts all instances of Test to Rest)

```
hren -o Test -n Rest
```

2. Ignore Complete Folders (ignores folders named venv/ node_modules and lib/ and its contents)

```
hren -o Test -n Rest -ifd "[venv, node_modules, lib]"
```

2. Ignore Certain Files (ignores files named test.py and hello.js)

```
hren -o Test -n Rest -ifl "[hello.js, test.py]"
```

3. Ignore all files with particular file extensions (ignores files with .pyc and .exe extension)

```
hren -o Test -n Rest -ie "[.pyc, .exe]"
```
   

## Bugs and Problems
1. You cannot run this script inside a folder that you want to rename. For example, If youre in a folder named Test/ and inside it you change Test/ to Rest/ It will fail as it cannot access the folder when it is open in the commandline. To perform that action you must go one directory above and then run the command
2. You cannot run this script directly in a drive volume for example: You cant run this script for a folder located in C: or E:, F: etc. It must be run inside a folder (This is because, the program will go through the entire folder structure, and since your system volume drives have so much data, it will take forever
3. You must not be inside a folder name that you want to rename to. For example, if youre in a folder named Rest and you want to change Test to Rest, you cant do that while youre inside Rest. You must go one level up!

These are bugs and i will fix them at some point! If you can contribute feel free to do so!
