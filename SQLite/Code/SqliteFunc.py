#!/usr/bin/env python3

# region Imports
import datetime
import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView
from sqlite3 import connect, Error

# My code
from Code.QueryTable import QueryTable


# endregion Imports


# region Code
# Used to store the sqlite credentials
class SQlite_Credentials:
    # Initialize class
    def __init__(self, database):
        self.database = database


# Used to get sqlite and put it into a table, well data frame then qt model
class sqlite_Into_Table:
    # Initialize class
    def __init__(self, table, query, sqlite):
        # Initial Set Up
        self.table = table
        self.query = query
        self.database = sqlite.database
        self.sqlite_Into_Table()

    # Function sqlite into Table
    def sqlite_Into_Table(self):
        # Create cursor for query
        try:
            connection = connect(self.database)
            cursor = connection.cursor()
            cursor.execute(self.query)
            query_data = cursor.fetchall()
            query_headers = list(
                cursor.description
            )  # list(map(lambda x: x[0], cursor.description))
            # Title the headers
            for pos in range(0, len(query_headers)):
                query_headers[pos] = str(query_headers[pos][0]).title()
            # Creating a pandas data frame
            sql_panda = pd.DataFrame(query_data)
            # Can't set headers if it's empty for whatever reason
            if not sql_panda.empty:
                sql_panda.columns = query_headers
            # Have to do the following to reformat date and some values. Uh oh nesting galore.
            # Check the table name
            table_name = self.table.objectName()
            # If the table is the log table
            if table_name == "LogTable":
                # Check every column
                for col in sql_panda:
                    # If the column is the duration column
                    if col == "Duration":
                        # For every row/cell in that column
                        for row, value in enumerate(sql_panda[col]):
                            sql_panda.loc[row, col] = datetime.datetime.strptime(
                                value, "%Y-%m-%d %H:%M:%S"
                            ).time()
            # This is probably a bad idea (possibly too many iterations), but if it's nan replace it with None
            for col in sql_panda:
                # For every row/cell in that column, replace unwanted displays with what I want (pd.isna should cover None's, Nan's and Nat's I believe)
                for row, value in enumerate(sql_panda[col]):
                    if pd.isna(value):
                        sql_panda.loc[row, col] = "None"
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
                    self.table.setColumnWidth(head, int(column_hint * 1.2))
                    horizonal_header.setSectionResizeMode(
                        head, QHeaderView.ResizeMode.Interactive
                    )
            vertical_header = self.table.verticalHeader()
            # Set the size of the rows based on the size hint for said row (makes the table nice and readable)
            for head in range(0, len(vertical_header)):
                row_hint = self.table.sizeHintForRow(head)
                self.table.setRowHeight(head, int(row_hint * 1.2))
            # Close the cursor and connection
            cursor.close()
            connection.close()
        except Error as error:
            return str(error)


# Used for general sqlite queries
class sqlite_General_Query:
    # Initialize class
    def __init__(self, query, sqlite):
        self.query = query
        self.database = sqlite.database

    # Function for general sqlite queries
    def sqlite_General_Query(self):
        try:
            connection = connect(self.database)
            cursor = connection.cursor()
            cursor.execute(self.query)
            connection.commit()
            cursor.close()
            connection.close()
            return "Successful Query"
        except Error as error:
            return str(error)


# Used for sqlite queries that return a value
class sqlite_Return_Query:
    # Initialize class
    def __init__(self, query, sqlite):
        self.query = query
        self.database = sqlite.database

    # Function for sqlite returning queries
    def sqlite_Return_Query(self):
        try:
            connection = connect(self.database)
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


# Used for handling null values and pseudo null values (for SQL) [SQL IS NULL NOT NONE YOU GOOSE! NONE IS PYTHON!]
class Process_Null:
    # Initialize class
    def __init__(self, modify):
        self.modify = modify

    # Function for trying to handle null values
    def Null_Values(self):
        # Make the values into a list (don't pass a string)
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
            if value == "None" or pd.isna(value):
                value = ""
            results.append(value)
        return results


# Used to create the tables if they don't exist
class Sqlite_Create_Tables:
    # Initialize class
    def __init__(self, sqlite):
        self.database = sqlite.database

    # Function for sqlite returning queries
    def Sqlite_Create_Tables(self):
        try:
            connection = connect(self.database)
            cursor = connection.cursor()
            create_customers = """
                CREATE TABLE IF NOT EXISTS Customers (
                    customerId INTEGER,
                    companyName VARCHAR(128),
                    contactName VARCHAR(32),
                    email VARCHAR(48),
                    phoneNumber VARCHAR (15),
                    socialMedia VARCHAR(64),
                    address VARCHAR(128),
                    lastOrder DATE,
                    lastFinishedOrder DATE,
                    status TEXT,
                    note TEXT,
                    PRIMARY KEY (customerId),
                    CONSTRAINT valid_status CHECK ((status) IN ("Good Standing","On The Fence","Blacklisted"))
                )
                """
            cursor.execute(create_customers)
            create_orders = """
                CREATE TABLE IF NOT EXISTS Orders (
                    orderId INTEGER,
                    orderName VARCHAR(64) UNIQUE NOT NULL,
                    customer INT NOT NULL,
                    note TEXT,
                    orderDate DATE NOT NULL,
                    plannedDate DATE NOT NULL,
                    finalDate DATE,
                    price DECIMAL(6,2),
                    paymentType VARCHAR(32),
                    status TEXT,
                    PRIMARY KEY (orderId),
                    FOREIGN KEY (customer) REFERENCES Customers(customerId),
                    CONSTRAINT planned_after_order CHECK (plannedDate >= orderDate),
                    CONSTRAINT final_after_order CHECK (finalDate >= orderDate),
                    CONSTRAINT valid_status CHECK ((status) IN ("Production", "Sold", "Cancelled", "Preorder","No Payment","Late"))
                )
                """
            cursor.execute(create_orders)
            create_items = """
                CREATE TABLE IF NOT EXISTS Items (
                    itemId INTEGER,
                    itemName VARCHAR(64) UNIQUE NOT NULL,
                    price DECIMAL(6,2) NOT NULL,
                    PRIMARY KEY (itemId)
                )
                """
            cursor.execute(create_items)
            create_activity = """
                CREATE TABLE IF NOT EXISTS Activity (
                    activityId INTEGER,
                    activityName VARCHAR(64) UNIQUE NOT NULL,
                    PRIMARY KEY (activityId)
                )
                """
            cursor.execute(create_activity)
            create_order_items = """
                CREATE TABLE IF NOT EXISTS OrderItems (
                    id INTEGER,
                    orderName VARCHAR(64) NOT NULL,
                    itemName VARCHAR(64) NOT NULL,
                    quantity DECIMAL(5,3) NOT NULL,
                    price DECIMAL(6,2),
                    note VARCHAR(64),
                    PRIMARY KEY (id),
                    FOREIGN KEY (orderName) REFERENCES Orders(orderName),
                    FOREIGN KEY (itemName) REFERENCES Items(itemName),
                    UNIQUE (orderName, itemName, note)
                )
                """
            cursor.execute(create_order_items)
            create_log = """
                CREATE TABLE IF NOT EXISTS Log (
                    logId INTEGER,
                    date DATE GENERATED ALWAYS AS (DATE(startTime)) STORED NOT NULL,
                    startTime DATETIME NOT NULL,
                    endTime DATETIME NOT NULL,
                    duration TIME NOT NULL,
                    note Text,
                    activity VARCHAR(64) NOT NULL,
                    orderName VARCHAR(64) NOT NULL,
                    PRIMARY KEY (logId),
                    FOREIGN KEY (activity) REFERENCES Activity(activityName),
                    FOREIGN KEY (orderName) REFERENCES Orders(orderName),
                    CONSTRAINT same_day CHECK (DATE(startTime) = DATE(endTime)),
                    CONSTRAINT positive_duration CHECK (duration > 0)
                )
                """
            cursor.execute(create_log)
            connection.commit()
            cursor.close()
            connection.close()
            return "Successful Query"
        except Error as error:
            return str(error)


# endregion Code
