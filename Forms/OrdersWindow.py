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
        # Update table
        self.updateTable()

    # Slot for opening the customers window
    def openCustomers(self):
        window = CustomersWindow.CustomersWindow(self.mysql_cred, self)
        window.show()

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

    # Slot for updating the table
    def updateTable(self):
        Query = f"SELECT * FROM orders"
        MySQL_Into_Table(self.ui.OrderTable, Query, self.mysql_cred)

        # Getting the selected Row

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
        Query = f'UPDATE orders SET orderName="{values[0]}", customer="{values[1]}", note="{values[2]}", orderDate="{values[3]}", plannedDate="{values[4]}", finalDate="{values[5]}", price="{values[6]}", status="{values[7]}" WHERE orderId={value}'
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
        Query = f"DELETE FROM orders WHERE orderId={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
