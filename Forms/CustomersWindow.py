#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog

# My UI
import UI.Customers as Customers

# My code
from Mine.MySQLFunc import MySQL_Into_Table
from Mine.MySQLFunc import MYSQL_General_Query

# endregion Imports

# region Code


# Defining the Customers Window
class CustomersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Customers.Ui_CustomerDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Table clicked
        self.ui.CustomerTable.clicked.connect(self.updateValues)
        # Load table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM customers"
        MySQL_Into_Table(self.ui.CustomerTable, Query, self.mysql_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.CustomerTable.currentIndex()
        row = cell.row()
        # Get the model
        model = self.ui.CustomerTable.model()
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
        self.ui.CompanyText.setText(results[1])
        self.ui.ContactText.setText(results[2])
        self.ui.EmailText.setText(results[3])
        self.ui.PhoneText.setText(results[4])
        self.ui.SocialText.setText(results[5])
        self.ui.AddressText.setText(results[6])
        self.ui.StatusBox.setCurrentText(results[9])
        self.ui.NoteText.setText(results[10])

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
        social = self.ui.SocialText.text()
        address = self.ui.AddressText.text()
        status = self.ui.StatusBox.currentText()
        note = self.ui.NoteText.toPlainText()
        return company_name, contact_name, email, phone, social, address, status, note

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO customers VALUES (NULL, "{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", "{values[4]}", "{values[5]}", NULL, NULL, "{values[6]}", "{values[7]}")'
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
        Query = f'UPDATE customers SET companyName="{values[0]}", contactName="{values[1]}", email="{values[2]}", phoneNumber="{values[3]}", socialMedia="{values[4]}, address="{values[5]}", status="{values[6]}", note="{values[7]}" WHERE customerId={value}'
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
        Query = f"DELETE FROM customers WHERE customerId={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
