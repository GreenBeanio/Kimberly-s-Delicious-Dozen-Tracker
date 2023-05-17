# region Imports
from PyQt6.QtCore import Qt, QAbstractTableModel, QAbstractItemModel

# import pandas as pd

# endregion Imports


# Class for creating table models for the table views to use
class QueryTable(QAbstractTableModel):
    # Initialize table
    def __init__(self, data, header):
        # Initial Set Up
        super().__init__()
        self._data = data
        self._header = header

    # All of these are functions inherited from QAbstractTableModel

    # Define the data
    def data(self, index, role):
        # If the cell (index) is displayed
        if role == Qt.ItemDataRole.DisplayRole:
            # Get the content of the cell from the pandas data frame
            contents = self._data.iloc[index.row(), index.column()]
            # Return the contents
            return str(contents)
            # I want to make this center the text, but I can't figure out how. I might have to switch to a tablewidget instead.

    # Defining the rows
    def rowCount(self, index):
        # Return the row count from pandas
        return len(self._data)

    # Defining the columns
    def columnCount(self, index):
        # Return the column count from pandas
        return len(self._data.columns)
        # return len(self._data[0])

    # Defining the column text
    def headerData(self, section, orientation, role):
        # If the section is displayed
        if role == Qt.ItemDataRole.DisplayRole:
            # If it is a horizontal header
            if orientation == Qt.Orientation.Horizontal:
                # Return the headers name
                return self._header[section]
