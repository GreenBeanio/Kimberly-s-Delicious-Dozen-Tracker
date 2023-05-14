#!/usr/bin/env python3

# region Imports
from PyQt6.QtWidgets import QApplication
import json
import sys
from mysql.connector import connect, Error
import datetime

# My code
from Mine.MySQLFunc import MYSQL_Credentials

# My Forms
import Forms.MainWindow as MainWindow

# endregion Imports

# region Parameters
# Empty variables for mysql
mysql_cred = ""
# endregion Parameters

# region Code


# Function to exit and record failure
def failure(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Write to a text file the error
    with open("failure.txt", "a+") as file:
        file.write(f"{current_time}\n{message}\n====================\n")
    # Close
    sys.exit()


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


# Function to connect to MySQL
def connect_to_mysql():
    try:
        with connect(
            host=mysql_cred.host,
            user=mysql_cred.user,
            password=mysql_cred.password,
            database=mysql_cred.database,
        ) as connection:
            return connection, "Connection"
    except Error as error:
        return error, "Failure"


# endregion Code

# Load the configuration file for mysql
mysql_cred = load_config()
# Test that mysql is working
mysql_connection, mysql_status = connect_to_mysql()
# If a error was given then exit the application
if mysql_status == "Failure":
    failure(mysql_connection)

# Main App Launching
app = QApplication(sys.argv)
win = MainWindow.MainWindow(mysql_cred)
win.show()
sys.exit(app.exec())
