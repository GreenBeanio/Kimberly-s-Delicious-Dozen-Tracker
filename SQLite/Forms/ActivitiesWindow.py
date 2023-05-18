#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QApplication

# My UI
import UI.Activities as Activities

# My code
from Code.SqliteFunc import sqlite_Into_Table
from Code.SqliteFunc import sqlite_General_Query
from Code.SqliteFunc import Process_Null


# endregion Imports


# region Code
# Defining the Activities Window
class ActivitiesWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, sqlite_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Activities.Ui_ActivitiesDialog()
        self.ui.setupUi(self)
        self.sqlite_cred = sqlite_cred
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        self.ui.Reload.clicked.connect(self.updateTable)
        # Change Search Enable
        self.ui.EnableSearch.stateChanged.connect(self.updateTable)
        # Changed searches
        self.ui.SearchText.textChanged.connect(self.updateTable)
        # Table clicked
        self.ui.ActivityTable.clicked.connect(self.updateValues)
        # Load the table
        self.updateTable()

    # Function to create sql
    def Create_SQL(self, start):
        # Used to store the query
        if start == "":
            sql = "SELECT * FROM activity"
        else:
            sql = start
        # Get the enabled status of the options
        searchEnabled = self.ui.EnableSearch.isChecked()
        # If the search is enabled
        if searchEnabled:
            # Get the sql
            sql = f'{sql} WHERE activityName LIKE "%{self.ui.SearchText.text()}%"'
        # Order by the activityName, because I think that'll be better with the activity naming convention being used
        sql = f"{sql} ORDER BY activityName"
        return sql

    # Slot for updating the table
    def updateTable(self):
        Query = self.Create_SQL("")
        sqlite_Into_Table(self.ui.ActivityTable, Query, self.sqlite_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.ActivityTable.currentIndex()
        row = cell.row()
        # Get the model
        model = self.ui.ActivityTable.model()
        # Get the index and value
        index = model.index(row, 1)
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Set the results into the elements
        self.ui.ActivityText.setText(value)
        # Get the current column and save it to your clipboard
        col = cell.column()
        QApplication.clipboard().setText(value)

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
        activity = self.ui.ActivityText.text()
        # Doing this for other code to work properly
        blank = ""
        return activity, blank

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values_data = self.GetValues()
        values = Process_Null(values_data)
        values = values.Null_Values()
        # Create query
        Query = f"INSERT INTO activity VALUES (NULL, {values[0]})"
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
            Query = (
                f"UPDATE activity SET activityName={values[0]} WHERE activityId={value}"
            )
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
        Query = f"DELETE FROM activity WHERE activityId={value}"
        # Get result of the query
        query_result = sqlite_General_Query(Query, self.sqlite_cred)
        result = query_result.sqlite_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
