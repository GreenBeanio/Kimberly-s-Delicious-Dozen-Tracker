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
        # If the index is displayed
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        # If the index is for setting the alignment
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

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
