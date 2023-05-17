#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog

# My UI
import UI.Activities as Activities

# My code
from Mine.MySQLFunc import MySQL_Into_Table
from Mine.MySQLFunc import MYSQL_General_Query
from Mine.MySQLFunc import Process_Null


# endregion Imports


# region Code
# Defining the Activities Window
class ActivitiesWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Activities.Ui_ActivitiesDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        self.ui.Reload.clicked.connect(self.updateTable)
        # Changed searches
        self.ui.SearchText.textChanged.connect(self.updateTable)
        # Table clicked
        self.ui.ActivityTable.clicked.connect(self.updateValues)
        # Load the table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM activity ORDER BY activityName"
        MySQL_Into_Table(self.ui.ActivityTable, Query, self.mysql_cred)

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
            Query = (
                f"UPDATE activity SET activityName={values[0]} WHERE activityId={value}"
            )
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
        Query = f"DELETE FROM activity WHERE activityId={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
