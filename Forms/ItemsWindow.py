#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog

# My UI
import UI.Items as Items

# My code
from Mine.MySQLFunc import MySQL_Into_Table
from Mine.MySQLFunc import MYSQL_General_Query

# endregion Imports


# region Code
# Defining the Items Window
class ItemsWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Items.Ui_ItemsDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Table clicked
        self.ui.ItemTable.clicked.connect(self.updateValues)
        # Load table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM items"
        MySQL_Into_Table(self.ui.ItemTable, Query, self.mysql_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.ItemTable.currentIndex()
        row = cell.row()
        # Get the model
        model = self.ui.ItemTable.model()
        # Get the index and column count
        index = model.index(row, 0)
        column_count = model.columnCount(index)
        # List to hold results
        results = []
        # Get the value from each column in the row
        for col in range(0, column_count):
            index = model.index(row, col)
            value = model.data(index, Qt.ItemDataRole.DisplayRole)
            results.append(value)
        # Set the results into the elements
        self.ui.ItemText.setText(results[1])
        self.ui.PriceText.setText(results[2])

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
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
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
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
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
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
