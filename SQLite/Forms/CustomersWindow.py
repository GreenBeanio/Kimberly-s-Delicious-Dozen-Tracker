#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QDialog, QApplication
import datetime

# My UI
import UI.Customers as Customers

# My code
from Code.SqliteFunc import sqlite_Into_Table
from Code.SqliteFunc import sqlite_General_Query
from Code.SqliteFunc import Process_Null
from Code.SqliteFunc import Display_Values

# endregion Imports

# region Code


# Defining the Customers Window
class CustomersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, sqlite_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Customers.Ui_CustomerDialog()
        self.ui.setupUi(self)
        self.sqlite_cred = sqlite_cred
        # Buttons
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        self.ui.GetStartDate.clicked.connect(self.Get_Date)
        self.ui.GetEndDate.clicked.connect(self.Get_Date)
        self.ui.Reload.clicked.connect(self.updateTable)
        self.ui.UpdateDates.clicked.connect(self.updateDates)
        # Change Search Enable
        self.ui.CompanyEnable.stateChanged.connect(self.updateTable)
        self.ui.EmailEnable.stateChanged.connect(self.updateTable)
        self.ui.SocialEnable.stateChanged.connect(self.updateTable)
        self.ui.ContactEnable.stateChanged.connect(self.updateTable)
        self.ui.PhoneEnable.stateChanged.connect(self.updateTable)
        self.ui.AddressEnable.stateChanged.connect(self.updateTable)
        self.ui.StatusEnable.stateChanged.connect(self.updateTable)
        self.ui.EnableDate.stateChanged.connect(self.updateTable)
        # Changed searches
        self.ui.CompanySearch.textChanged.connect(self.updateTable)
        self.ui.ContactSearch.textChanged.connect(self.updateTable)
        self.ui.EmailSearch.textChanged.connect(self.updateTable)
        self.ui.PhoneSearch.textChanged.connect(self.updateTable)
        self.ui.SocialSearch.textChanged.connect(self.updateTable)
        self.ui.AddressSearch.textChanged.connect(self.updateTable)
        self.ui.StatusComboSearch.currentTextChanged.connect(self.updateTable)
        self.ui.DateSelection.currentTextChanged.connect(self.updateTable)
        self.ui.StartDate.dateChanged.connect(self.updateTable)
        self.ui.EndDate.dateChanged.connect(self.updateTable)
        # Table clicked
        self.ui.CustomerTable.clicked.connect(self.updateValues)
        # Load table
        self.updateTable()

    # Function to create sql
    def Create_SQL(self, start):
        # Used to store the query
        if start == "":
            sql = "SELECT * FROM customers"
        else:
            sql = start
        # Get the enabled status of the options
        companyEnabled = self.ui.CompanyEnable.isChecked()
        emailEnabled = self.ui.EmailEnable.isChecked()
        socialEnabled = self.ui.SocialEnable.isChecked()
        contactEnabled = self.ui.ContactEnable.isChecked()
        phoneEnabled = self.ui.PhoneEnable.isChecked()
        addressEnabled = self.ui.AddressEnable.isChecked()
        statusEnabled = self.ui.StatusEnable.isChecked()
        dateEnabled = self.ui.EnableDate.isChecked()
        # If any of the search options are enabled
        if (
            companyEnabled
            or emailEnabled
            or socialEnabled
            or contactEnabled
            or phoneEnabled
            or addressEnabled
            or statusEnabled
            or dateEnabled
        ):
            sql = f"{sql} WHERE "
        # If the company search is enabled
        if companyEnabled:
            # Get the sql
            sql = f'{sql}companyName LIKE "%{self.ui.CompanySearch.text()}%"'
            # Check if any down the line are enabled
            if (
                emailEnabled
                or socialEnabled
                or contactEnabled
                or phoneEnabled
                or addressEnabled
                or statusEnabled
                or dateEnabled
            ):
                sql = f"{sql} AND "
        # If the email search is enabled
        if emailEnabled:
            # Get the sql
            sql = f'{sql}email LIKE "%{self.ui.EmailSearch.text()}%"'
            # Check if any down the line are enabled
            if (
                socialEnabled
                or contactEnabled
                or phoneEnabled
                or addressEnabled
                or statusEnabled
                or dateEnabled
            ):
                sql = f"{sql} AND "
        # If the social search is enabled
        if socialEnabled:
            # Get the sql
            sql = f'{sql}socialMedia LIKE "%{self.ui.SocialSearch.text()}%"'
            # Check if any down the line are enabled
            if (
                contactEnabled
                or phoneEnabled
                or addressEnabled
                or statusEnabled
                or dateEnabled
            ):
                sql = f"{sql} AND "
        # If the contact search is enabled
        if contactEnabled:
            # Get the sql
            sql = f'{sql}contactName LIKE "%{self.ui.ContactSearch.text()}%"'
            # Check if any down the line are enabled
            if phoneEnabled or addressEnabled or statusEnabled or dateEnabled:
                sql = f"{sql} AND "
        # If the phone search is enabled
        if phoneEnabled:
            # Get the sql
            sql = f'{sql}phoneNumber LIKE "%{self.ui.PhoneSearch.text()}%"'
            # Check if any down the line are enabled
            if addressEnabled or statusEnabled or dateEnabled:
                sql = f"{sql} AND "
        # If the address search is enabled
        if addressEnabled:
            # Get the sql
            sql = f'{sql}address LIKE "%{self.ui.AddressSearch.text()}%"'
            # Check if any down the line are enabled
            if statusEnabled or dateEnabled:
                sql = f"{sql} AND "
        # If the status search is enabled
        if statusEnabled:
            # Get the sql
            sql = f'{sql}status = "{self.ui.StatusComboSearch.currentText()}"'
            # Check if any down the line are enabled
            if dateEnabled:
                sql = f"{sql} AND "
        # If the date search is enabled
        if dateEnabled:
            # Get the type of date we're searching for
            date_type = self.ui.DateSelection.currentText()
            if date_type == "Last Order":
                date_type = "lastOrder"
            elif date_type == "Last Finished Order":
                date_type = "lastFinishedOrder"
            # Get the date values
            start_date = self.ui.StartDate.date().toString("yyyy-MM-dd")
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = self.ui.EndDate.date().toString("yyyy-MM-dd")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            values_data = [start_date, end_date]
            values = Process_Null(values_data)
            values = values.Null_Values()
            # If the start date isn't null
            if values[0] != "Null":
                # if the end date isn't null
                if values[1] != "Null":
                    sql = f'{sql}{date_type} BETWEEN "{self.ui.StartDate.date().toString("yyyy-MM-dd")}" AND "{self.ui.EndDate.date().toString("yyyy-MM-dd")}"'
                else:
                    sql = f'{sql}{date_type} = "{self.ui.StartDate.date().toString("yyyy-MM-dd")}"'
                # Order it by the selected date because why not (might remove this later)
                sql = f"{sql} ORDER BY {date_type}"
        return sql

    # Function to get the date
    def Get_Date(self):
        result = datetime.date.today()
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "GetStartDate":
            self.ui.StartDate.setDate(QDate(result))
        elif pressed == "GetEndDate":
            self.ui.EndDate.setDate(QDate(result))

    # Function to update the dates
    def updateDates(self):
        # Update the last order
        Query = "UPDATE Customers SET lastOrder = (SELECT orderDate FROM Orders WHERE orderDate IS NOT NULL AND customer=Customers.customerId ORDER BY orderDate DESC LIMIT 1)"
        query_result = sqlite_General_Query(Query, self.sqlite_cred)
        result = query_result.sqlite_General_Query()
        self.ui.OutputText.setText(result)
        # Update the last finished order
        Query = "UPDATE Customers SET lastFinishedOrder = (SELECT finalDate FROM Orders WHERE finalDate IS NOT NULL AND customer=Customers.customerId ORDER BY finalDate DESC LIMIT 1)"
        query_result = sqlite_General_Query(Query, self.sqlite_cred)
        result = query_result.sqlite_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Slot for updating the table
    def updateTable(self):
        Query = self.Create_SQL("")
        sqlite_Into_Table(self.ui.CustomerTable, Query, self.sqlite_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.CustomerTable.currentIndex()
        # Get the model
        model = self.ui.CustomerTable.model()
        # Get the values
        results = Display_Values(model, cell)
        results = results.Display_Values()
        # Set the results into the elements
        self.ui.CompanyText.setText(results[1])
        self.ui.ContactText.setText(results[2])
        self.ui.EmailText.setText(results[3])
        self.ui.PhoneText.setText(results[4])
        self.ui.SocialText.setText(results[5])
        self.ui.AddressText.setText(results[6])
        self.ui.StatusBox.setCurrentText(results[9])
        self.ui.NoteText.setText(results[10])
        # Get the current column and save it to your clipboard!
        col = cell.column()
        QApplication.clipboard().setText(results[col])

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
        values_data = self.GetValues()
        values = Process_Null(values_data)
        values = values.Null_Values()
        # Create query
        Query = f"INSERT INTO customers VALUES (NULL, {values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]}, NULL, NULL, {values[6]}, {values[7]})"
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
            Query = f"UPDATE customers SET companyName={values[0]}, contactName={values[1]}, email={values[2]}, phoneNumber={values[3]}, socialMedia={values[4]}, address={values[5]}, status={values[6]}, note={values[7]} WHERE customerId={value}"
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
        Query = f"DELETE FROM customers WHERE customerId={value}"
        # Get result of the query
        query_result = sqlite_General_Query(Query, self.sqlite_cred)
        result = query_result.sqlite_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
