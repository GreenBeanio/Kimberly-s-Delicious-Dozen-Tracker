#!/usr/bin/env python3

# region Imports
from PyQt6.QtWidgets import QApplication
import sys

# My code
from Mine.SqliteFunc import SQlite_Credentials
from Mine.SqliteFunc import Sqlite_Create_Tables

# My Forms
import Forms.MainWindow as MainWindow

# endregion Imports

# region Code
# Create sqlite database (if it doesn't exist)
sqlite_cred = SQlite_Credentials("test.db")
sqlcon = Sqlite_Create_Tables(sqlite_cred)
sqlcon.Sqlite_Create_Tables()
# Main App Launching
app = QApplication(sys.argv)
win = MainWindow.MainWindow(sqlite_cred)
win.show()
sys.exit(app.exec())

# endregion Code
