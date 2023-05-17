#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QDialog
import datetime

# My UI
import UI.Orders as Orders

# My code
from Mine.MySQLFunc import MySQL_Into_Table
from Mine.MySQLFunc import MYSQL_General_Query
from Mine.MySQLFunc import Process_Null
from Mine.MySQLFunc import Display_Values
from Mine.MySQLFunc import MYSQL_Return_Query

# My Forms
import Forms.CustomersWindow as CustomersWindow

# endregion Imports


# region Code
# Defining the Orders Window
class OrdersWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Orders.Ui_OrdersDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.CustomersButton.clicked.connect(self.openCustomers)
        self.ui.GetOrderDateButton.clicked.connect(self.GetDate)
        self.ui.GetPlannedDateButton.clicked.connect(self.GetDate)
        self.ui.GetFinalDateButton.clicked.connect(self.GetDate)
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        self.ui.ResetButton.clicked.connect(self.ResetDate)
        self.ui.CalculatePrice.clicked.connect(self.CalculatePrice)
        self.ui.GetTotalSales.clicked.connect(self.TotalSales)
        self.ui.Reload.clicked.connect(self.updateTable)
        self.ui.CalculatePrice.clicked.connect(self.updatePrice)
        # Changed searches
        self.ui.OrderSearchText.textChanged.connect(self.updateTable)
        self.ui.CustomerSearchText.textChanged.connect(self.updateTable)
        self.ui.StatusComboSearch.currentTextChanged.connect(self.updateTable)
        self.ui.DateTypeBox.currentTextChanged.connect(self.updateTable)
        self.ui.StartDateSelect.dateChanged.connect(self.updateTable)
        self.ui.EndDateSelect.dateChanged.connect(self.updateTable)
        # Table clicked
        self.ui.OrderTable.clicked.connect(self.updateValues)
        # Update table
        self.updateTable()

    # Slot for opening the customers window
    def openCustomers(self):
        window = CustomersWindow.CustomersWindow(self.mysql_cred, self)
        window.show()

    # To reset the date for pseudo null value
    def ResetDate(self):
        self.ui.FinalDate.setDate(QDate(2000, 1, 1))

    # Get the date
    def GetDate(self):
        result = datetime.date.today()
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "GetOrderDateButton":
            self.ui.OrderDate.setDate(QDate(result))
        elif pressed == "GetPlannedDateButton":
            self.ui.PlannedDate.setDate(QDate(result))
        elif pressed == "GetFinalDateButton":
            self.ui.FinalDate.setDate(QDate(result))

    # Calculate the price from the items in the order
    def CalculatePrice(self):
        Query = f'SELECT SUM(price) FROM orderitems WHERE orderName="{self.ui.OrderText.text()}"'
        result = MYSQL_Return_Query(Query, self.mysql_cred)
        result = result.MYSQL_Return_Query()
        self.ui.PriceText.setText(result)

    # Function to create sql
    def Create_SQL(self, start):
        # Used to store the query
        if start == "":
            sql = "SELECT * FROM orders"
        else:
            sql = start
        # Get the enabled status of the options
        orderEnabled = self.ui.OrderEnable.isChecked()
        customerEnabled = self.ui.CustomerEnable.isChecked()
        statusEnabled = self.ui.StatusEnable.isChecked()
        dateEnabled = self.ui.EnableDate.isChecked()
        # If any of the search options are enabled
        if orderEnabled or customerEnabled or statusEnabled or dateEnabled:
            sql = f"{sql} WHERE "
        # If the order search is enabled
        if orderEnabled:
            # Get the sql
            sql = f'{sql}orderName LIKE "%{self.ui.OrderSearchText.text()}%"'
            # Check if any down the line are enabled
            if customerEnabled or statusEnabled or dateEnabled:
                sql = f"{sql} AND "
        # If the customer search is enabled
        if customerEnabled:
            # Get the sql
            sql = f'{sql}customer = "{self.ui.CustomerSearchText.text()}"'
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
            date_type = self.ui.DateTypeBox.currentText()
            if date_type == "Order Date":
                date_type = "orderDate"
            elif date_type == "Planned Date":
                date_type = "plannedDate"
            elif date_type == "Final Date":
                date_type = "finalDate"
            # Get the date values
            start_date = self.ui.StartDateSelect.date().toString("yyyy-MM-dd")
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = self.ui.EndDateSelect.date().toString("yyyy-MM-dd")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            values_data = [start_date, end_date]
            values = Process_Null(values_data)
            values = values.Null_Values()
            # If the start date isn't null
            if values[0] != "Null":
                # if the end date isn't null
                if values[1] != "Null":
                    sql = f'{sql}{date_type} BETWEEN "{self.ui.StartDateSelect.date().toString("yyyy-MM-dd")}" AND "{self.ui.EndDateSelect.date().toString("yyyy-MM-dd")}"'
                else:
                    sql = f'{sql}{date_type} = "{self.ui.StartDateSelect.date().toString("yyyy-MM-dd")}"'
                # Order it by the selected date because why not (might remove this later)
                sql = f"{sql} ORDER BY {date_type}"
        return sql

    # Calculate the price from the items in the order
    def TotalSales(self):
        Query = self.Create_SQL("SELECT SUM(price) FROM orders")
        result = MYSQL_Return_Query(Query, self.mysql_cred)
        result = result.MYSQL_Return_Query()
        self.ui.TotalSales.setText(result)

    # Slot for updating the price
    def updatePrice(self):
        # Update the last order
        Query = self.Create_SQL(
            "UPDATE Orders SET price = (SELECT SUM(price) FROM OrderItems WHERE orderName=Orders.orderName) WHERE price IS NULL"
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
        MySQL_Into_Table(self.ui.OrderTable, Query, self.mysql_cred)

        # Getting the selected Row

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.OrderTable.currentIndex()
        # Get the model
        model = self.ui.OrderTable.model()
        # Get the values
        results = Display_Values(model, cell)
        results = results.Display_Values()
        # Set the results into the elements
        self.ui.OrderText.setText(results[1])
        self.ui.CustomerText.setText(results[2])
        self.ui.NoteText.setText(results[3])
        self.ui.OrderDate.setDate(QDate.fromString(results[4], "yyyy-MM-dd"))
        self.ui.PlannedDate.setDate(QDate.fromString(results[5], "yyyy-MM-dd"))
        if results[6] == "":
            self.ui.FinalDate.setDate(QDate(2000, 1, 1))
        else:
            self.ui.FinalDate.setDate(QDate.fromString(results[6], "yyyy-MM-dd"))
        self.ui.PriceText.setText(results[7])
        self.ui.PaymentText.setText(results[8])
        self.ui.StatusBox.setCurrentText(results[9])

    # Get the selected row
    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.OrderTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.OrderTable.model()
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
        payment = self.ui.PaymentText.text()
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
            payment,
            status,
        )

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values_data = self.GetValues()
        values = Process_Null(values_data)
        values = values.Null_Values()
        # Create query
        Query = f"INSERT INTO orders VALUES (NULL, {values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]}, {values[6]}, {values[7]}, {values[8]})"
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
            Query = f"UPDATE orders SET orderName={values[0]}, customer={values[1]}, note={values[2]}, orderDate={values[3]}, plannedDate={values[4]}, finalDate={values[5]}, price={values[6]}, paymentType={values[7]}, status={values[8]} WHERE orderId={value}"
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
        Query = f"DELETE FROM orders WHERE orderId={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
