#!/usr/bin/env python3

# region Imports
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QPushButton,
    QGridLayout,
    QMessageBox,
    QComboBox,
    QLineEdit,
    QDialog,
    QTableWidget,
)
from PyQt6.QtGui import QIcon, QDoubleValidator
from pathlib import Path
import json
import sys
import os
from mysql.connector import connect, Error
import datetime

# My UI
import UI.Activities as Activities
import UI.Customers as Customers
import UI.Items as Items
import UI.Log as Log
import UI.Main as Main
import UI.OrderItems as OrderItems
import UI.Orders as Orders

# endregion Imports

# region Parameters

# Empty variables for mysql
host = ""
user = ""
password = ""
mysql_connection = ""
mysql_status = ""
# Qt UI files

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
        return host, user, password


def connect_to_mysql():
    try:
        with connect(host=host, user=user, password=password) as connection:
            return connection, "Connection"
    except Error as error:
        return error, "Failure"


# Load the configuration file
host, user, password = load_config()
# connect to mysql
mysql_connection, mysql_status = connect_to_mysql()
# If a error was given then exit the application
if mysql_status == "Failure":
    failure(mysql_connection)
print(mysql_connection)
# endregion Code


# Defining the Main Window
class MainWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Main.Ui_MainDialog()
        self.ui.setupUi(self)
        # Buttons
        self.ui.ActivitiesButton.clicked.connect(self.openWindow)
        self.ui.CustomersButton.clicked.connect(self.openWindow)
        self.ui.ItemsButton.clicked.connect(self.openWindow)
        self.ui.LogButton.clicked.connect(self.openWindow)
        self.ui.OrderItemsButton.clicked.connect(self.openWindow)
        self.ui.OrdersButton.clicked.connect(self.openWindow)

    # Slot for opening the other windows
    def openWindow(self):
        window = ""
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        print(pressed)
        if pressed == "ActivitiesButton":
            window = ActivitiesWindow(self)
        elif pressed == "CustomersButton":
            window = CustomersWindow(self)
        elif pressed == "ItemsButton":
            window = ItemsWindow(self)
        elif pressed == "LogButton":
            window = LogWindow(self)
        elif pressed == "OrderItemsButton":
            window = OrderItemsWindow(self)
        elif pressed == "OrdersButton":
            window = OrdersWindow(self)
        # Open the selected window
        window.exec()


# Defining the Activities Window
class ActivitiesWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Activities.Ui_ActivitiesDialog()
        self.ui.setupUi(self)


# Defining the Customers Window
class CustomersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Customers.Ui_CustomerDialog()
        self.ui.setupUi(self)


# Defining the Log Window
class LogWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Log.Ui_LogDialog()
        self.ui.setupUi(self)


# Defining the Items Window
class ItemsWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Items.Ui_ItemsDialog()
        self.ui.setupUi(self)


# Defining the OrderItems Window
class OrderItemsWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = OrderItems.Ui_OrderItemsDialog()
        self.ui.setupUi(self)


# Defining the Orders Window
class OrdersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Orders.Ui_OrdersDialog()
        self.ui.setupUi(self)


# Main App Launching
app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())
