# region Imports
from PyQt6.QtCore import Qt, QAbstractTableModel

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

    # Define the data
    def data(self, index, role):
        # Do this or it's all kinds of messed up
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])

    # Defining the rows
    def rowCount(self, index):
        return len(self._data)

    # Defining the columns
    def columnCount(self, index):
        return len(self._data.columns)
        # return len(self._data[0])

    # Defining the column text
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._header[section]
