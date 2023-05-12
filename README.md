# Kimberly's Delicious Dozen Tracker

## What Does It Do?

### FILL IN ###

## Reason For Creation

### FILL IN ###

## Running The Python Script

### Windows

- Initial Run
  - cd /your/folder
  - python3 -m venv env
  - call env/Scripts/activate.bat
    - If using powershell instead of cmd do
      - ./env/Scripts/Activate.ps1
  - python3 -m pip install -r requirements.txt
  - python3 KDD.py
- Running After
  - cd /your/folder
  - call env/Scripts/activate.bat && python3 KDD.py
    - If using powershell instead of cmd do
      - ./env/Scripts/Activate.ps1 && python3 KDD.py
- Running Without Terminal Staying Around
  - Change the file type from py to pyw
  - You should just be able to click the file to launch it
  - May need to also change python3 to just python if it doesn't work after the change
    - In the first line of the code change python3 to python

### Linux

- Initial Run
  - cd /your/folder
  - python3 -m venv env
  - source env/bin/activate
  - python3 -m pip install -r requirements.txt
  - python3 KDD.py
- Running After
  - cd /your/folder
  - source env/bin/activate && python3 KDD.py
- Running Without Terminal Staying Around
  - Run the file with nohup
  - May have to set executable if it's not already
    - chmod +x KDD.py
