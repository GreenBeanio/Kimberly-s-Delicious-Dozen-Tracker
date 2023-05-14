#!/usr/bin/env python3

from PyQt6 import uic
from pathlib import Path
import os
import subprocess
import sys

# Parameters
UI_Path = "UI_RAW/"
Save_Path = "UI/"

# Convert
UI_Path = Path(UI_Path)
Save_Path = Path(Save_Path)

# List of the files in the directory
ui_to_convert = os.listdir(UI_Path)


# Check for existence of paths
def check_directory(directory, type):
    if not directory.is_dir():
        return f"{type}"
    else:
        return ""


# Compile every .ui file
def convert_ui():
    for ui in ui_to_convert:
        # Full UI Path
        full_path = Path(UI_Path, ui)
        if full_path.is_file():
            new_name = full_path.stem
            new_path = Path(Save_Path, f"{new_name}.py")
            subprocess.run(
                ["pyuic6", f"{full_path}", "-o", f"{new_path}"],
                shell=False,
                capture_output=True,
                text=True,
            )


# If the source ui directory doesn't exist stop the script
result = check_directory(UI_Path, "UI")
if result != "":
    print(f"Invalid ui path to directory!")
    input()
    sys.exit()
# If the save path doesn't exist then make it
result = check_directory(Save_Path, "Save")
if result != "":
    os.mkdir(Save_Path)

# Compile the ui files to python
convert_ui()
