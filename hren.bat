@echo off
set "script_path=%~dp0"
set "script_path=%script_path%hyper_rename.py"
python %script_path% %CD% %*