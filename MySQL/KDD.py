#!/usr/bin/env python3

# region Imports
from PyQt6.QtWidgets import QApplication
import json
import sys

# My code
from Code.MySQLFunc import MYSQL_Credentials

# My Forms
import Forms.MainWindow as MainWindow

# endregion Imports


# region Code
# Function to load from the configuration file
def load_config():
    with open("config.json", "r") as config:
        raw = json.load(config)
        mysql = raw["mysql"]
        host = mysql["Host"]
        user = mysql["User"]
        password = mysql["Password"]
        database = mysql["Database"]
        mysql_cred = MYSQL_Credentials(host, user, password, database)
        return mysql_cred


# Load the configuration file for mysql
mysql_cred = load_config()
# Main App Launching
app = QApplication(sys.argv)
win = MainWindow.MainWindow(mysql_cred)
win.show()
sys.exit(app.exec())

# endregion Code
