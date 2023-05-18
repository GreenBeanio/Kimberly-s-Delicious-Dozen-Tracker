#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QApplication

# My UI
import UI.Items as Items

# My code
from Code.SqliteFunc import sqlite_Into_Table
from Code.SqliteFunc import sqlite_General_Query
from Code.SqliteFunc import Process_Null
from Code.SqliteFunc import Display_Values

# endregion Imports


# region Code
# Defining the Items Window
class ItemsWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, sqlite_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Items.Ui_ItemsDialog()
        self.ui.setupUi(self)
        self.sqlite_cred = sqlite_cred
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        self.ui.Reload.clicked.connect(self.updateTable)
        # Changed searches
        self.ui.SearchText.textChanged.connect(self.updateTable)
        # Table clicked
        self.ui.ItemTable.clicked.connect(self.updateValues)
        # Load table
        self.updateTable()

    # Function to create sql
    def Create_SQL(self, start):
        # Used to store the query
        if start == "":
            sql = "SELECT * FROM items"
        else:
            sql = start
        # Get the enabled status of the options
        searchEnabled = self.ui.EnableSearch.isChecked()
        # If the search is enabled
        if searchEnabled:
            # Get the sql
            sql = f'{sql} WHERE itemName LIKE "%{self.ui.SearchText.text()}%"'
        # Order by the itemName (might change this later)
        sql = f"{sql} ORDER BY itemName"
        return sql

    # Slot for updating the table
    def updateTable(self):
        Query = self.Create_SQL("")
        sqlite_Into_Table(self.ui.ItemTable, Query, self.sqlite_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.ItemTable.currentIndex()
        # Get the model
        model = self.ui.ItemTable.model()
        # Get the values
        results = Display_Values(model, cell)
        results = results.Display_Values()
        # Set the results into the elements
        self.ui.ItemText.setText(results[1])
        self.ui.PriceText.setText(results[2])
        # Get the current column and save it to your clipboard!
        col = cell.column()
        QApplication.clipboard().setText(results[col])

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
        item_name = self.ui.ItemText.text()
        item_price = self.ui.PriceText.text()
        return item_name, item_price

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values_data = self.GetValues()
        values = Process_Null(values_data)
        values = values.Null_Values()
        # Create query
        Query = f"INSERT INTO items VALUES (NULL, {values[0]}, {values[1]})"
        # Get result of the query
        query_result = sqlite_General_Query(Query, self.sqlite_cred)
        result = query_result.sqlite_General_Query()
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
            Query = f"UPDATE items SET itemName={values[0]}, price={values[1]} WHERE itemId={value}"
            # Get result of the query
            query_result = sqlite_General_Query(Query, self.sqlite_cred)
            result = query_result.sqlite_General_Query()
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
        Query = f"DELETE FROM items WHERE itemId={value}"
        # Get result of the query
        query_result = sqlite_General_Query(Query, self.sqlite_cred)
        result = query_result.sqlite_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
