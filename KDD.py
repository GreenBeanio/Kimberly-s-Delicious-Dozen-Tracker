#!/usr/bin/env python3

# region Imports
import typing
from PyQt6.QtCore import Qt, QAbstractTableModel
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
    QTableWidgetItem,
    QTableView,
    QHeaderView,
)
from PyQt6.QtGui import QIcon, QDoubleValidator
from pathlib import Path
import json
import sys
import os
from mysql.connector import connect, Error
import datetime
import pandas

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
database = ""
mysql_connection = ""
mysql_status = ""
# Qt UI files

# endregion Parameters

# region Code


# Function MySQL into Table
def MySQL_Into_Table(table, query):
    # Create cursor for query
    try:
        # Can't use the mysql connection from earlier. Does it have to be 1 every time?
        connection = connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM log")
        query_data = cursor.fetchall()
        query_headers = cursor.column_names
        # Use pandas to filter the data (convert datetimes to strings and such)
        ################
        # Use setheaderData to set the headers to column names???

        # Make a model for the view?
        Table = QueryTable(query_data, query_headers)

        table.setModel(Table)
        print("success")
    except Error as error:
        print(error)


class QueryTable(QAbstractTableModel):
    # Initialize table
    def __init__(self, data, header):
        # Initial Set Up
        super().__init__()
        self._data = data
        self._header = header

    # Define the data
    def data(self, index, role):
        # Do this or it's all kinds of messed up
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    # Defining the rows
    def rowCount(self, index):
        return len(self._data)

    # Defining the columns
    def columnCount(self, index):
        return len(self._data[0])

    # Defining the column text
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._header[section]


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
        return host, user, password, database


# Function to connect to MySQL
def connect_to_mysql():
    try:
        with connect(
            host=host, user=user, password=password, database=database
        ) as connection:
            return connection, "Connection"
    except Error as error:
        return error, "Failure"


# Function to get the current date
def GetDate():
    return "Wow A date"


# Function to get the current time
def GetTime():
    return "Wow A time"


# Load the configuration file
host, user, password, database = load_config()
# connect to mysql
mysql_connection, mysql_status = connect_to_mysql()
# If a error was given then exit the application
if mysql_status == "Failure":
    failure(mysql_connection)
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
        # Buttons
        self.ui.GetDateButton.clicked.connect(self.Get_Date)
        self.ui.GetStartButton.clicked.connect(self.Get_Time)
        self.ui.GetEndButton.clicked.connect(self.Get_Time)
        self.ui.ShowActivitiesButton.clicked.connect(self.openWindow)
        self.ui.ShowOrdersButton.clicked.connect(self.openWindow)
        # Load Table
        MySQL_Into_Table(self.ui.LogTable, "test")

    # Function to get the date
    def Get_Date(self):
        result = GetDate()
        print(result)

    # Function to get the time
    def Get_Time(self):
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "GetStartButton":
            result = GetTime()
            print(result)
            print("That's a start time")
        elif pressed == "GetEndButton":
            result = GetTime()
            print(result)
            print("That's an end time")

    # Slot for opening the other windows
    def openWindow(self):
        window = ""
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        print(pressed)
        if pressed == "ShowActivitiesButton":
            window = ActivitiesWindow(self)
        elif pressed == "ShowOrdersButton":
            window = OrdersWindow(self)
        # Open the selected window
        window.exec()


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
        # Buttons
        self.ui.OrdersButton.clicked.connect(self.openWindow)
        self.ui.ItemsButton.clicked.connect(self.openWindow)

    # Slot for opening the other windows
    def openWindow(self):
        window = ""
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        print(pressed)
        if pressed == "OrdersButton":
            window = OrdersWindow(self)
        elif pressed == "ItemsButton":
            window = ItemsWindow(self)
        # Open the selected window
        window.exec()


# Defining the Orders Window
class OrdersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Orders.Ui_OrdersDialog()
        self.ui.setupUi(self)
        # Buttons
        self.ui.CustomersButton.clicked.connect(self.openCustomers)
        self.ui.GetDateButton.clicked.connect(self.GetDate)

    # Slot for opening the customers window
    def openCustomers(self):
        window = CustomersWindow(self)
        window.exec()

    # Get the date
    def GetDate(self):
        result = GetDate()
        print(result)


# Main App Launching
app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())
