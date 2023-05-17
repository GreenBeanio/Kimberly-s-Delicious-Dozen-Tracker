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
from Mine.MySQLFunc import Process_Null
from Mine.MySQLFunc import Display_Values
from Mine.MySQLFunc import MYSQL_Return_Query

# My Forms
import Forms.ActivitiesWindow as ActivitiesWindow
import Forms.OrdersWindow as OrdersWindow

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
        self.ui.GetDateStartDate.clicked.connect(self.Get_Date)
        self.ui.GetDateEndDate.clicked.connect(self.Get_Date)
        self.ui.GetTotalHours.clicked.connect(self.TotalHours)
        self.ui.Reload.clicked.connect(self.updateTable)
        # Changed Searches
        # self.ui.OrderSearch.returnPressed.connect(self.updateTable)
        self.ui.OrderSearch.textChanged.connect(self.updateTable)
        self.ui.ActivitySearch.textChanged.connect(self.updateTable)
        self.ui.StartDate.dateChanged.connect(self.updateTable)
        self.ui.EndDate.dateChanged.connect(self.updateTable)
        # Table clicked
        self.ui.LogTable.clicked.connect(self.updateValues)
        # Load Table on load
        self.updateTable()
        self.ui.LogTable

    # Function to create sql
    def Create_SQL(self, start):
        # Used to store the query
        if start == "":
            sql = "SELECT * FROM log"
        else:
            sql = start
        # Get the enabled status of the options
        orderEnabled = self.ui.EnableOrder.isChecked()
        activityEnabled = self.ui.EnableActivity.isChecked()
        startDateEnabled = self.ui.EnableStart.isChecked()
        endDateEnabled = self.ui.EnableEnd.isChecked()
        # If any of the options are enabled (except for endDate, which needs startDate to work)
        if orderEnabled or activityEnabled or startDateEnabled:
            sql = f"{sql} WHERE "
        # If the order is enabled
        if orderEnabled:
            # Get the sql
            sql = f'{sql}orderName LIKE "%{self.ui.OrderSearch.text()}%"'
            # Check if any down the line are enabled
            if activityEnabled or startDateEnabled:
                sql = f"{sql} AND "
        # If the activity is enabled
        if activityEnabled:
            # Get the sql
            sql = f'{sql}activity LIKE "%{self.ui.ActivitySearch.text()}%"'
            # Check if any down the line are enabled
            if startDateEnabled:
                sql = f"{sql} AND "
        # If the start date is enabled
        if startDateEnabled:
            # If the endDate is also enabled use a range
            if endDateEnabled:
                sql = f'{sql}date BETWEEN "{self.ui.StartDate.date().toString("yyyy-MM-dd")}" AND "{self.ui.EndDate.date().toString("yyyy-MM-dd")}"'
            # If the endDate isn't enabled search for just that date
            else:
                sql = f'{sql}date = "{self.ui.StartDate.date().toString("yyyy-MM-dd")}"'
        # Order the results by the date and then start time, heck even end time why not
        sql = f"{sql} ORDER BY date, startTime, endTime"
        return sql

    def TotalHours(self):
        # Not that due to mysql having a max time value of 839:59:59 I will not use it. Instead I will use a datetime.
        # sql = self.Create_SQL("SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(duration))) FROM log")
        sql = self.Create_SQL("SELECT SUM(TIME_TO_SEC(duration)) FROM log")
        response = MYSQL_Return_Query(sql, self.mysql_cred)
        response = response.MYSQL_Return_Query()
        response = datetime.timedelta(seconds=float(response))
        # Different format for the time delta because I want HH:MM:SS not days HH:MM:SS, heck not even the seconds
        minutes, seconds = divmod(response.seconds + response.days * 86400, 60)
        hours, minutes = divmod(minutes, 60)
        # days, hours = divmod(hours, 24)
        # output = f"{hours}:{minutes}:{seconds}"
        # output = f"{hours}:{minutes}"
        # output = f"Days: {days} | Hours: {hours} | Minutes: {minutes}"
        output = f"Hours: {hours} | Minutes: {minutes}"
        self.ui.TotalHours.setText(output)

    # Function to get the date
    def Get_Date(self):
        result = datetime.date.today()
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "GetDateButton":
            self.ui.DataSelect.setDate(QDate(result))
        elif pressed == "GetDateStartDate":
            self.ui.StartDate.setDate(QDate(result))
        elif pressed == "GetDateEndDate":
            self.ui.EndDate.setDate(QDate(result))

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
        if pressed == "ShowActivitiesButton":
            window = ActivitiesWindow.ActivitiesWindow(self.mysql_cred, self)
        elif pressed == "ShowOrdersButton":
            window = OrdersWindow.OrdersWindow(self.mysql_cred, self)
        # Open the selected window
        window.show()

    # Slot for updating the table
    def updateTable(self):
        # date_selection = self.ui.DataSelect.date().toString("yyyy-MM-dd")
        # Query = f'SELECT * FROM log WHERE date = "{date_selection}" ORDER BY date, startTime'
        Query = self.Create_SQL("")
        MySQL_Into_Table(self.ui.LogTable, Query, self.mysql_cred)

    # Slot for updating the values in the fields based off the table clicked
    def updateValues(self):
        # Get the current location in the table
        cell = self.ui.LogTable.currentIndex()
        # Get the model
        model = self.ui.LogTable.model()
        # Get the values
        results = Display_Values(model, cell)
        results = results.Display_Values()
        # Set the results into the elements
        self.ui.DataSelect.setDate(QDate.fromString(results[1], "yyyy-MM-dd"))
        self.ui.StartSelect.setTime(QTime.fromString(results[2], "HH:mm:ss"))
        self.ui.EndSelect.setTime(QTime.fromString(results[3], "HH:mm:ss"))
        self.ui.NoteBox.setText(results[5])
        self.ui.ActivitiesText.setText(results[6])
        self.ui.OrderText.setText(results[7])

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
        # Get the actual value of the cell if one was actually selected
        try:
            value = model.data(index, Qt.ItemDataRole.DisplayRole)
        except:
            value = "Nothing Selected"
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
        activity = self.ui.ActivitiesText.text()
        orderName = self.ui.OrderText.text()
        return start_time, end_time, note, activity, orderName

    # Slot for Adding an entry
    def AddEntry(self):
        # Get element values
        values_data = self.GetValues()
        values = Process_Null(values_data)
        values = values.Null_Values()
        # Create query
        Query = f"INSERT INTO log (startTime, endTime, note, activity, orderName) VALUES ({values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]})"
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
        # If something was selected
        if value != "Nothing Selected":
            # Get element values
            values_data = self.GetValues()
            values = Process_Null(values_data)
            values = values.Null_Values()
            # Query to update the value
            Query = f"UPDATE log SET startTime={values[0]}, endTime={values[1]}, note={values[2]}, activity={values[3]}, orderName={values[4]} WHERE logid={value}"
            # Get result of the query
            query_result = MYSQL_General_Query(Query, self.mysql_cred)
            result = query_result.MYSQL_General_Query()
            self.ui.OutputText.setText(result)
            # Reload the table
            self.updateTable()
        # If something wasn't selected
        else:
            self.ui.OutputText.setText(value)

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


# endregion Code
