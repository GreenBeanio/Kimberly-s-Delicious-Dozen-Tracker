#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog

# My UI
import UI.OrderItems as OrderItems

# My code
from Mine.MySQLFunc import MySQL_Into_Table
from Mine.MySQLFunc import MYSQL_General_Query
from Mine.MySQLFunc import Display_Values
from Mine.MySQLFunc import MYSQL_Return_Query

# My Forms
import Forms.ItemsWindow as ItemsWindow
import Forms.OrdersWindow as OrdersWindow
from Mine.MySQLFunc import Process_Null


# endregion Imports


# region Code
# Defining the OrderItems Window
class OrderItemsWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = OrderItems.Ui_OrderItemsDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.OrdersButton.clicked.connect(self.openWindow)
        self.ui.ItemsButton.clicked.connect(self.openWindow)
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        self.ui.CalculatePrice.clicked.connect(self.CalculatePrice)
        self.ui.Reload.clicked.connect(self.updateTable)
        self.ui.CalculatePrice.clicked.connect(self.updatePrice)
        # Changed searches
        self.ui.OrderSearchText.textChanged.connect(self.updateTable)
        self.ui.ItemSearchText.textChanged.connect(self.updateTable)
        # Table clicked
        self.ui.OrderItemTable.clicked.connect(self.updateValues)
        # Load Table on load
        self.updateTable()

    # Function to create sql
    def Create_SQL(self, start):
        # Used to store the query
        if start == "":
            sql = "SELECT * FROM orderitems"
        else:
            sql = start
        # Get the enabled status of the options
        orderEnabled = self.ui.EnableOrder.isChecked()
        itemEnabled = self.ui.EnableItem.isChecked()
        # If either search is enabled
        if orderEnabled or itemEnabled:
            sql = f"{sql} WHERE "
        # If the order search is enabled
        if orderEnabled:
            # Get the sql
            sql = f'{sql}orderName LIKE "%{self.ui.OrderSearchText.text()}%"'
            # Check if item is also enabled
            if itemEnabled:
                sql = f"{sql} AND "
        # If the item search is enabled
        if itemEnabled:
            # Get the sql
            sql = f'{sql}itemName LIKE "%{self.ui.ItemSearchText.text()}%"'
        # Order by the orderName then itemName (might change this later)
        sql = f"{sql} ORDER BY orderName, itemName"
        return sql

    # Slot for opening the other windows
    def openWindow(self):
        window = ""
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "OrdersButton":
            window = OrdersWindow.OrdersWindow(self.mysql_cred, self)
        elif pressed == "ItemsButton":
            window = ItemsWindow.ItemsWindow(self.mysql_cred, self)
        # Open the selected window
        window.show()

    # Calculate the price from the items in the order
    def CalculatePrice(self):
        Query = f'SELECT DISTINCT {self.ui.QuantityText.text()} * (SELECT price FROM Items WHERE itemName="{self.ui.ItemText.text()}") FROM orderitems'
        result = MYSQL_Return_Query(Query, self.mysql_cred)
        result = result.MYSQL_Return_Query()
        self.ui.PriceText.setText(result)

    # Slot for updating the price
    def updatePrice(self):
        # Update the last order
        Query = self.Create_SQL(
            "UPDATE OrderItems SET price = quantity * (SELECT price FROM Items WHERE itemName=OrderItems.itemName) WHERE price IS NULL;"
        )
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = self.Create_SQL("")
        MySQL_Into_Table(self.ui.OrderItemTable, Query, self.mysql_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.OrderItemTable.currentIndex()
        # Get the model
        model = self.ui.OrderItemTable.model()
        # Get the values
        results = Display_Values(model, cell)
        results = results.Display_Values()
        # Set the results into the elements
        self.ui.OrderText.setText(results[1])
        self.ui.ItemText.setText(results[2])
        self.ui.QuantityText.setText(results[3])
        self.ui.PriceText.setText(results[4])
        self.ui.NoteText.setText(results[5])

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
        # Get the actual value of the cell if one was actually selected
        try:
            value = model.data(index, Qt.ItemDataRole.DisplayRole)
        except:
            value = "Nothing Selected"
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
        values_data = self.GetValues()
        values = Process_Null(values_data)
        values = values.Null_Values()
        # Create query
        Query = f"INSERT INTO orderitems VALUES (NULL, {values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]})"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        if value != "Nothing Selected":
            # Get element values
            values_data = self.GetValues()
            values = Process_Null(values_data)
            values = values.Null_Values()
            # Create query
            Query = f"UPDATE orderitems SET orderName={values[0]}, itemName={values[1]}, quantity={values[2]}, price={values[3]}, note={values[4]} WHERE id={value}"
            # Get result of the query
            query_result = MYSQL_General_Query(Query, self.mysql_cred)
            result = query_result.MYSQL_General_Query()
            self.ui.OutputText.setText(result)
            # Reload the table
            self.updateTable()
        else:
            self.ui.OutputText.setText(value)

    # Slot for Deleting an entry
    def DeleteEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Query to delete the entry
        Query = f"DELETE FROM orderitems WHERE id={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
