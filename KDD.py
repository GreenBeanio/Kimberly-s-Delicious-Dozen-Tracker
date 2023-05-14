#!/usr/bin/env python3

# region Imports
import typing
from PyQt6.QtCore import Qt, QAbstractTableModel, QDate, QTime
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
import pandas as pd

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

# endregion Parameters

# region Code


# Function MySQL into Table
def MySQL_Into_Table(table, query):
    # Create cursor for query
    try:
        # Can't use the mysql connection from earlier. Does it have to be 1 every time?
        connection = connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        cursor.execute(query)
        query_data = cursor.fetchall()
        query_headers = list(cursor.column_names)
        # Title the headers
        for pos in range(1, len(query_headers)):
            query_headers[pos] = query_headers[pos].title()
        # Used to print out query data
        # for row_number, row in enumerate(query_data):
        #     print(f"Row {row_number}")
        #     for column_number, column in enumerate(row):
        #         print(
        #             f"{query_headers[column_number]}: {column} : Type: {type(column)}"
        #         )
        # Creating a pandas data frame
        sql_panda = pd.DataFrame(query_data)
        # Can't set headers if it's empty for whatever reason
        if not sql_panda.empty:
            sql_panda.columns = query_headers
        # For every column that is a datetime, convert it to time
        for col in sql_panda.select_dtypes(include=["datetime64[ns]"]).columns.tolist():
            sql_panda[col] = sql_panda[col].dt.time
        # For every column that is a tiemdelta, do some real convoluted stuff to show it as a time
        for col in sql_panda.select_dtypes(
            include=["timedelta64[ns]"]
        ).columns.tolist():
            # For every timedelta in the column
            for index, delta in enumerate(sql_panda[col]):
                # Convert the timedelta into seconds and then a datetime
                sql_panda.loc[index, col] = datetime.datetime.utcfromtimestamp(
                    delta.total_seconds()
                )  # .strftime("%H:%M:%S")
            # Convert the new times to a datetime and then only show the time
            sql_panda[col] = pd.to_datetime(sql_panda[col]).dt.time
        # Make the table model
        Table = QueryTable(sql_panda, query_headers)
        # Set the table views model
        table.setModel(Table)
    except Error as error:
        ### Will return this to the little error label in the future possibly
        print(error)


# Function for general mysql queries
def MYSQL_General_Query(query):
    try:
        connection = connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return "Successful Query"
    except Error as error:
        return str(error)


# Function to get lists of query results
def MYSQL_Query_List(query):
    try:
        connection = connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        cursor.execute(query)
        query_data = cursor.fetchall()
        return query_data
    except Error as error:
        return error


# Class for creating tables
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
            return str(self._data.iloc[index.row(), index.column()])
            # return str(self._data.iloc[index.row(), index.column()])
            # return self._data[index.row()][index.column()]

    # Defining the rows
    def rowCount(self, index):
        return len(self._data)

    # Defining the columns
    def columnCount(self, index):
        return len(self._data.columns)
        # return len(self._data[0])

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
    return datetime.date.today()


# Function to get the current time
def GetTime():
    return datetime.datetime.now()


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
        window.show()


# Defining the Activities Window
class ActivitiesWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Activities.Ui_ActivitiesDialog()
        self.ui.setupUi(self)
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Load the table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM activity ORDER BY activityName"
        MySQL_Into_Table(self.ui.ActivityTable, Query)

    # Getting the selected Row
    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.ActivityTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.ActivityTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get element values
        activity = self.ui.ActivityText.text()
        return activity

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO activity VALUES (NULL, "{values}")'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'UPDATE activity SET activityName="{values}" WHERE activityId={value}'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM activity WHERE activityId={value}"
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# Defining the Customers Window
class CustomersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Customers.Ui_CustomerDialog()
        self.ui.setupUi(self)
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Load table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM customers"
        MySQL_Into_Table(self.ui.CustomerTable, Query)

    # Getting the selected Row
    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.CustomerTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.CustomerTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get element values
        company_name = self.ui.CompanyText.text()
        contact_name = self.ui.ContactText.text()
        email = self.ui.EmailText.text()
        phone = self.ui.PhoneText.text()
        address = self.ui.AddressText.text()
        status = self.ui.StatusBox.currentText()
        note = self.ui.NoteText.toPlainText()
        return company_name, contact_name, email, phone, address, status, note

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO customers VALUES (NULL, "{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", "{values[4]}", NULL, NULL, "{values[5]}", "{values[6]}")'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'UPDATE customers SET companyName="{values[0]}", contactName="{values[1]}", email="{values[2]}", phoneNumber="{values[3]}", address="{values[4]}", status="{values[5]}", note="{values[6]}" WHERE customerId={value}'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM customers WHERE customerId={value}"
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


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
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Date selection changed
        self.ui.DataSelect.dateChanged.connect(self.updateTable)
        # Load Table on load
        self.updateTable()
        # Load foreign keys into the combo boxes
        self.Add_To_Combo()

    # Function to get the date
    def Get_Date(self):
        result = GetDate()
        self.ui.DataSelect.setDate(QDate(result))

    # Function to get the time
    def Get_Time(self):
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "GetStartButton":
            result = GetTime()
            self.ui.StartSelect.setTime(QTime(result.time()))
        elif pressed == "GetEndButton":
            result = GetTime()
            self.ui.EndSelect.setTime(QTime(result.time()))

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
        window.show()
        # window.exec()

    # Slot for updating the table
    def updateTable(self):
        date_selection = self.ui.DataSelect.date().toString("yyyy-MM-dd")
        # date_selection = self.ui.DataSelect.date().toString("yyyy.MM.dd")
        # date_selection = datetime.datetime.strptime(date_selection, "%Y.%m.%d")
        # date_selection = date_selection.strftime("%Y-%m-%d")
        Query = f'SELECT * FROM log WHERE date = "{date_selection}" ORDER BY startTime'
        MySQL_Into_Table(self.ui.LogTable, Query)

    # Getting the selected Row
    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.LogTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.LogTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get date
        date_selection = self.ui.DataSelect.date().toString("yyyy-MM-dd")
        date_selection = datetime.datetime.strptime(date_selection, "%Y-%m-%d").date()
        # Get start time
        start_time = self.ui.StartSelect.time().toString("hh:mm")
        start_time = datetime.datetime.strptime(start_time, "%H:%M").time()
        start_time = datetime.datetime.combine(date_selection, start_time)
        # Get end time
        end_time = self.ui.EndSelect.time().toString("hh:mm")
        end_time = datetime.datetime.strptime(end_time, "%H:%M").time()
        end_time = datetime.datetime.combine(date_selection, end_time)
        # Get others
        note = self.ui.NoteBox.toPlainText()
        activity = self.ui.ActivitiesBox.currentText()
        orderName = self.ui.OrderBox.currentText()
        return start_time, end_time, note, activity, orderName

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO log (startTime, endTime, note, activity, orderName) VALUES ("{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", "{values[4]}")'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()
        ### This seems to crash for some reason if you press it twice... not sure why

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Query to update the value
        Query = f'UPDATE log SET startTime="{values[0]}", endTime="{values[1]}", note="{values[2]}", activity="{values[3]}", orderName="{values[4]}" WHERE logid={value}'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM log WHERE logid={value}"
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Combobox Items
    def Add_To_Combo(self):
        # Get the activities
        Query = f"SELECT activityName FROM activity"
        result = MYSQL_Query_List(Query)
        for entry in result:
            self.ui.ActivitiesBox.addItem(entry[0])
        # Get the orders
        Query = f"SELECT orderName FROM orders"
        result = MYSQL_Query_List(Query)
        for entry in result:
            self.ui.OrderBox.addItem(entry[0])


# Defining the Items Window
class ItemsWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Items.Ui_ItemsDialog()
        self.ui.setupUi(self)
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Load table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM items"
        MySQL_Into_Table(self.ui.ItemTable, Query)

    # Getting the selected Row
    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.ItemTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.ItemTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get element values
        item_name = self.ui.ItemText.text()
        item_price = self.ui.PriceText.text()
        return item_name, item_price

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO items VALUES (NULL, "{values[0]}", "{values[1]}")'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'UPDATE items SET itemName="{values[0]}", price="{values[1]}" WHERE itemId={value}'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM items WHERE itemId={value}"
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


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
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # OrderChanged
        self.ui.OrderText.textChanged.connect(self.updateTable)
        # Load Table on load
        self.updateTable()

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
        window.show()

    # Slot for updating the table
    def updateTable(self):
        orderName = self.ui.OrderText.text()
        Query = f'SELECT * FROM orderitems WHERE orderName = "{orderName}"'
        MySQL_Into_Table(self.ui.OrderItemTable, Query)

        # Getting the selected Row

    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.OrderItemTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.OrderItemTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get element values
        order_name = self.ui.OrderText.text()
        item = self.ui.ItemText.text()
        quantity = self.ui.QuantityText.text()
        price = self.ui.PriceText.text()
        note = self.ui.NoteText.toPlainText()
        return order_name, item, quantity, price, note

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO orderitems VALUES (NULL, "{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", "{values[4]}")'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'UPDATE orderitems SET orderName="{values[0]}", itemName="{values[1]}", quantity="{values[2]}", price="{values[3]}", note="{values[4]}" WHERE id={value}'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM orderitems WHERE id={value}"
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


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
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Update table
        self.updateTable()

    # Slot for opening the customers window
    def openCustomers(self):
        window = CustomersWindow(self)
        window.show()

    # Get the date
    def GetDate(self):
        result = GetDate()
        print(result)

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM orders"
        MySQL_Into_Table(self.ui.OrderTable, Query)

        # Getting the selected Row

    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.OrderTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.OrderTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get dates
        order_date = self.ui.OrderDate.date().toString("yyyy-MM-dd")
        order_date = datetime.datetime.strptime(order_date, "%Y-%m-%d").date()
        planned_date = self.ui.PlannedDate.date().toString("yyyy-MM-dd")
        planned_date = datetime.datetime.strptime(planned_date, "%Y-%m-%d").date()
        final_date = self.ui.FinalDate.date().toString("yyyy-MM-dd")
        final_date = datetime.datetime.strptime(final_date, "%Y-%m-%d").date()
        # Get other values
        order_name = self.ui.OrderText.text()
        customer = self.ui.CustomerText.text()
        price = self.ui.PriceText.text()
        status = self.ui.StatusBox.currentText()
        note = self.ui.NoteText.toPlainText()
        return (
            order_name,
            customer,
            note,
            order_date,
            planned_date,
            final_date,
            price,
            status,
        )

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO orders VALUES (NULL, "{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", "{values[4]}", "{values[5]}", "{values[6]}", "{values[7]}")'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'UPDATE orders SET orderName="{values[0]}", customer="{values[1]}", note="{values[2]}", orderDate="{values[3]}", plannedDate="{values[4]}", finalDate="{values[5]}", price="{values[6]}", status="{values[7]}" WHERE orderId={value}'
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM orders WHERE orderId={value}"
        # Get result of the query
        result = MYSQL_General_Query(Query)
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# Main App Launching
app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())
