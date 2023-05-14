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

# My Forms
import Forms.ItemsWindow as ItemsWindow
import Forms.OrdersWindow as OrdersWindow

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
        # OrderChanged
        self.ui.OrderText.textChanged.connect(self.updateTable)
        # Load Table on load
        self.updateTable()

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

    # Slot for updating the table
    def updateTable(self):
        orderName = self.ui.OrderText.text()
        Query = f'SELECT * FROM orderitems WHERE orderName = "{orderName}"'
        MySQL_Into_Table(self.ui.OrderItemTable, Query, self.mysql_cred)

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
        Query = f'UPDATE orderitems SET orderName="{values[0]}", itemName="{values[1]}", quantity="{values[2]}", price="{values[3]}", note="{values[4]}" WHERE id={value}'
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
        Query = f"DELETE FROM orderitems WHERE id={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()


# endregion Code
