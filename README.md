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
### 3. Add the directory path to your environment variables
### 4. now you can type "hren" in your cmd and it should work!
