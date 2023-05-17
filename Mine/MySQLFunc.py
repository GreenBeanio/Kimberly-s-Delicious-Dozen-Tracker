#!/usr/bin/env python3

# region Imports
from mysql.connector import connect, Error
import datetime
import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView

# My code
from Mine.QueryTable import QueryTable

# endregion Imports


# region Code
# Used to store the MySQL credentials
class MYSQL_Credentials:
    # Initialize class
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


# Used to get MySQL and put it into a table, well data frame then qt model
class MySQL_Into_Table:
    # Initialize class
    def __init__(self, table, query, mysql):
        # Initial Set Up
        self.table = table
        self.query = query
        self.host = mysql.host
        self.user = mysql.user
        self.password = mysql.password
        self.database = mysql.database
        self.MySQL_Into_Table()

    # Function MySQL into Table
    def MySQL_Into_Table(self):
        # Create cursor for query
        try:
            connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            cursor.execute(self.query)
            query_data = cursor.fetchall()
            query_headers = list(cursor.column_names)
            # Title the headers
            for pos in range(1, len(query_headers)):
                query_headers[pos] = query_headers[pos].title()
            # Creating a pandas data frame
            sql_panda = pd.DataFrame(query_data)
            # Can't set headers if it's empty for whatever reason
            if not sql_panda.empty:
                sql_panda.columns = query_headers
            # For every column that is a datetime, convert it to time
            for col in sql_panda.select_dtypes(
                include=["datetime64[ns]"]
            ).columns.tolist():
                sql_panda[col] = sql_panda[col].dt.time
            # For every column that is a tiemdelta, do some real convoluted stuff to show it as a time
            for col in sql_panda.select_dtypes(
                include=["timedelta64[ns]"]
            ).columns.tolist():
                # For every timedelta in the column
                for index, delta in enumerate(sql_panda[col]):
                    # Convert the timedelta into seconds and then a datetime
                    sql_panda.loc[index, col] = datetime.datetime.utcfromtimestamp(
                        delta.total_seconds()
                    )
                # Convert the new times to a datetime and then only show the time
                sql_panda[col] = pd.to_datetime(sql_panda[col]).dt.time
            # Make the table model
            Table = QueryTable(sql_panda, query_headers)
            # Set the table views model
            self.table.setModel(Table)
            # Set the size and types of the columns
            horizonal_header = self.table.horizontalHeader()
            for head in range(0, len(horizonal_header)):
                if head == 0:
                    horizonal_header.setSectionResizeMode(
                        head, QHeaderView.ResizeMode.ResizeToContents
                    )
                elif head == len(horizonal_header) - 1:
                    horizonal_header.setSectionResizeMode(
                        head, QHeaderView.ResizeMode.Stretch
                    )
                else:
                    column_hint = self.table.sizeHintForColumn(head)
                    self.table.setColumnWidth(head, column_hint * 1.2)
                    horizonal_header.setSectionResizeMode(
                        head, QHeaderView.ResizeMode.Interactive
                    )
            vertical_header = self.table.verticalHeader()
            # Set the size of the rows based on the size hint for said row (makes the table nice and readable)
            for head in range(0, len(vertical_header)):
                row_hint = self.table.sizeHintForRow(head)
                self.table.setRowHeight(head, row_hint * 1.2)
            # Close the cursor and connection
            cursor.close()
            connection.close()
        except Error as error:
            return str(error)


# Used for general MySQL queries
class MYSQL_General_Query:
    # Initialize class
    def __init__(self, query, mysql):
        self.query = query
        self.host = mysql.host
        self.user = mysql.user
        self.password = mysql.password
        self.database = mysql.database

    # Function for general mysql queries
    def MYSQL_General_Query(self):
        try:
            connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            cursor.execute(self.query)
            connection.commit()
            cursor.close()
            connection.close()
            return "Successful Query"
        except Error as error:
            return str(error)


# Used for MYSQL queries that return a value
class MYSQL_Return_Query:
    # Initialize class
    def __init__(self, query, mysql):
        self.query = query
        self.host = mysql.host
        self.user = mysql.user
        self.password = mysql.password
        self.database = mysql.database

    # Function for mysql returning queries
    def MYSQL_Return_Query(self):
        try:
            connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            cursor = connection.cursor()
            cursor.execute(self.query)
            query_data = cursor.fetchone()
            query_data = str(query_data[0])
            connection.commit()
            cursor.close()
            connection.close()
            if query_data != "None":
                return query_data
            else:
                return ""
        except Error as error:
            return ""


# Used for handling null values and pseudo null values (for SQL)
class Process_Null:
    # Initialize class
    def __init__(self, modify):
        self.modify = modify

    # Function for trying to handle null values
    def Null_Values(self):
        # If the value isn't a string then make it a list
        values = list(self.modify)
        # Attempting to allow for null values
        for index, value in enumerate(values):
            # If the value is a string
            if type(value) == str:
                # If it is empty then make it NULL
                if value == "":
                    values[index] = "NULL"
                # If it isn't empty surround it in quotes
                else:
                    values[index] = f'"{value}"'
            # If it's a datetime.datetime surround it in quotes
            elif type(value) == datetime.datetime:
                values[index] = f'"{value}"'
            # If it's a datetime.time surround it in quotes
            elif type(value) == datetime.time:
                values[index] = f'"{value}"'
            # If it's a date surround it in quotes
            elif type(value) == datetime.date:
                # If the date is the date for pseudo null treat it as such
                if value == datetime.date(2000, 1, 1):
                    values[index] = "NULL"
                # If it's a valid date, then treat it as such
                else:
                    values[index] = f'"{value}"'
        return values


# Used for modifying what is displayed in the elements from the table selection
class Display_Values:
    # Initialize class
    def __init__(self, model, cell):
        self.model = model
        self.cell = cell

    # Function to modify the values
    def Display_Values(self):
        # Get the current location in the table
        row = self.cell.row()
        # Get the index and column count
        index = self.model.index(row, 0)
        column_count = self.model.columnCount(index)
        # List to hold results
        results = []
        # Get the value from each column in the row
        for col in range(0, column_count):
            index = self.model.index(row, col)
            value = self.model.data(index, Qt.ItemDataRole.DisplayRole)
            # If the value is none set to blank?
            if value == "None":
                value = ""
            results.append(value)
        return results


# endregion Code
