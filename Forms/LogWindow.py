#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtCore import Qt, QDate, QTime
from PyQt6.QtWidgets import QDialog
import datetime

# My UI
import UI.Log as Log

# My code
from Mine.MySQLFunc import MySQL_Into_Table
from Mine.MySQLFunc import MYSQL_General_Query
from Mine.MySQLFunc import MYSQL_Query_List

# My Forms
import Forms.ActivitiesWindow as ActivitiesWindow
import Forms.CustomersWindow as CustomersWindow

# endregion Imports


# region Code
# Defining the Log Window
class LogWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Log.Ui_LogDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.GetDateButton.clicked.connect(self.Get_Date)
        self.ui.GetStartButton.clicked.connect(self.Get_Time)
        self.ui.GetEndButton.clicked.connect(self.Get_Time)
        self.ui.ShowActivitiesButton.clicked.connect(self.openWindow)
        self.ui.ShowOrdersButton.clicked.connect(self.openWindow)
        self.ui.AddButton.clicked.connect(self.AddEntry)
        self.ui.UpdateButton.clicked.connect(self.UpdateEntry)
        self.ui.DeleteButton.clicked.connect(self.DeleteEntry)
        # Date selection changed
        self.ui.DataSelect.dateChanged.connect(self.updateTable)
        # Load Table on load
        self.updateTable()
        # Load foreign keys into the combo boxes
        self.Add_To_Combo()

    # Function to get the date
    def Get_Date(self):
        result = datetime.date.today()
        self.ui.DataSelect.setDate(QDate(result))

    # Function to get the time
    def Get_Time(self):
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "GetStartButton":
            result = datetime.datetime.now()
            self.ui.StartSelect.setTime(QTime(result.time()))
        elif pressed == "GetEndButton":
            result = datetime.datetime.now()
            self.ui.EndSelect.setTime(QTime(result.time()))

    # Slot for opening the other windows
    def openWindow(self):
        window = ""
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        print(pressed)
        if pressed == "ShowActivitiesButton":
            window = ActivitiesWindow(self)
        elif pressed == "ShowOrdersButton":
            window = CustomersWindow(self)
        # Open the selected window
        window.show()
        # window.exec()

    # Slot for updating the table
    def updateTable(self):
        date_selection = self.ui.DataSelect.date().toString("yyyy-MM-dd")
        # date_selection = self.ui.DataSelect.date().toString("yyyy.MM.dd")
        # date_selection = datetime.datetime.strptime(date_selection, "%Y.%m.%d")
        # date_selection = date_selection.strftime("%Y-%m-%d")
        Query = f'SELECT * FROM log WHERE date = "{date_selection}" ORDER BY startTime'
        MySQL_Into_Table(self.ui.LogTable, Query, self.mysql_cred)

    # Getting the selected Row
    def SelectedRow(self):
        # Get the current selected cell
        cell = self.ui.LogTable.currentIndex()
        column = 0  # cell.column()
        row = cell.row()
        # Get the data model the table view is using
        model = self.ui.LogTable.model()
        # Get the index of the model from the cell earlier
        index = model.index(row, column)
        # Get the actual value of the cell
        value = model.data(index, Qt.ItemDataRole.DisplayRole)
        # Return the value
        return value

    # Function to get the information from gui elements
    def GetValues(self):
        # Get date
        date_selection = self.ui.DataSelect.date().toString("yyyy-MM-dd")
        date_selection = datetime.datetime.strptime(date_selection, "%Y-%m-%d").date()
        # Get start time
        start_time = self.ui.StartSelect.time().toString("hh:mm")
        start_time = datetime.datetime.strptime(start_time, "%H:%M").time()
        start_time = datetime.datetime.combine(date_selection, start_time)
        # Get end time
        end_time = self.ui.EndSelect.time().toString("hh:mm")
        end_time = datetime.datetime.strptime(end_time, "%H:%M").time()
        end_time = datetime.datetime.combine(date_selection, end_time)
        # Get others
        note = self.ui.NoteBox.toPlainText()
        activity = self.ui.ActivitiesBox.currentText()
        orderName = self.ui.OrderBox.currentText()
        return start_time, end_time, note, activity, orderName

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values = self.GetValues()
        # Create query
        Query = f'INSERT INTO log (startTime, endTime, note, activity, orderName) VALUES ("{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", "{values[4]}")'
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()
        ### This seems to crash for some reason if you press it twice... not sure why

    # Slot for Updating an entry
    def UpdateEntry(self):
        # Get the selected cell
        value = self.SelectedRow()
        # Get element values
        values = self.GetValues()
        # Query to update the value
        Query = f'UPDATE log SET startTime="{values[0]}", endTime="{values[1]}", note="{values[2]}", activity="{values[3]}", orderName="{values[4]}" WHERE logid={value}'
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
        Query = f"DELETE FROM log WHERE logid={value}"
        # Get result of the query
        query_result = MYSQL_General_Query(Query, self.mysql_cred)
        result = query_result.MYSQL_General_Query()
        self.ui.OutputText.setText(result)
        # Reload the table
        self.updateTable()

    # Combobox Items
    def Add_To_Combo(self):
        # Get the activities
        Query = f"SELECT activityName FROM activity"
        # Have to create an instance of the object for this to work
        query_list = MYSQL_Query_List(Query, self.mysql_cred)
        result = query_list.MYSQL_Query_List()
        print(result)
        for entry in result:
            self.ui.ActivitiesBox.addItem(entry[0])
        # Get the orders
        Query = f"SELECT orderName FROM orders"
        query_list = MYSQL_Query_List(Query, self.mysql_cred)
        result = query_list.MYSQL_Query_List()
        for entry in result:
            self.ui.OrderBox.addItem(entry[0])


# endregion Code
