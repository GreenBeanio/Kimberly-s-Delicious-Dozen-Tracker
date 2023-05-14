#!/usr/bin/env python3

# region Imports
from mysql.connector import connect, Error
import datetime
import pandas as pd

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
            # Can't use the mysql connection from earlier. Does it have to be 1 every time?
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
                    )  # .strftime("%H:%M:%S")
                # Convert the new times to a datetime and then only show the time
                sql_panda[col] = pd.to_datetime(sql_panda[col]).dt.time
            # Make the table model
            Table = QueryTable(sql_panda, query_headers)
            # Set the table views model
            self.table.setModel(Table)
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
            return "Successful Query"
        except Error as error:
            return str(error)


# Used to return a list of query results
class MYSQL_Query_List:
    # Initialize class
    def __init__(self, query, mysql):
        self.query = query
        self.host = mysql.host
        self.user = mysql.user
        self.password = mysql.password
        self.database = mysql.database

    # Function to get lists of query results
    def MYSQL_Query_List(self):
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
            return query_data
        except Error as error:
            return str(error)


# endregion Code
