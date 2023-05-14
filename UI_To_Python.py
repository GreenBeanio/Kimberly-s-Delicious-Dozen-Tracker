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

# To store bad paths
bad_paths = []

# List of the files in the directory
ui_to_convert = os.listdir(UI_Path)


# Stop if the paths are bad
def Invalid_Directory():
    for bad in bad_paths:
        print(f"Invalid {bad} path to directory!")
    input()
    sys.exit()


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


# Check that both paths are good
result = check_directory(UI_Path, "UI")
if result != "":
    bad_paths.append(result)
result = check_directory(Save_Path, "Save")
if result != "":
    bad_paths.append(result)
if len(bad_paths) != 0:
    Invalid_Directory()

# Compile the ui files to python
convert_ui()
