#!/usr/bin/env python3

# region Imports

# Packages
from PyQt6.QtWidgets import QDialog

# My UI
import UI.Main as Main

# My Forms
import Forms.ActivitiesWindow as ActivitiesWindow
import Forms.OrdersWindow as OrdersWindow
import Forms.ItemsWindow as ItemsWindow
import Forms.LogWindow as LogWindow
import Forms.OrderItemsWindow as OrderItemsWindow
import Forms.CustomersWindow as CustomersWindow

# endregion Imports


# region Code
# Defining the Main Window
class MainWindow(QDialog):
    # Initializing the Dialog
    def __init__(self, mysql_cred, parent=None):
        # Initial Set Up
        super().__init__(parent)
        self.ui = Main.Ui_MainDialog()
        self.ui.setupUi(self)
        self.mysql_cred = mysql_cred
        # Buttons
        self.ui.ActivitiesButton.clicked.connect(self.openWindow)
        self.ui.CustomersButton.clicked.connect(self.openWindow)
        self.ui.ItemsButton.clicked.connect(self.openWindow)
        self.ui.LogButton.clicked.connect(self.openWindow)
        self.ui.OrderItemsButton.clicked.connect(self.openWindow)
        self.ui.OrdersButton.clicked.connect(self.openWindow)

    # Slot for opening the other windows
    def openWindow(self):
        window = ""
        # Get the name of the button pressed
        pressed = self.sender().objectName()
        if pressed == "ActivitiesButton":
            window = ActivitiesWindow.ActivitiesWindow(self.mysql_cred, self)
        elif pressed == "CustomersButton":
            window = CustomersWindow.CustomersWindow(self.mysql_cred, self)
        elif pressed == "ItemsButton":
            window = ItemsWindow.ItemsWindow(self.mysql_cred, self)
        elif pressed == "LogButton":
            window = LogWindow.LogWindow(self.mysql_cred, self)
        elif pressed == "OrderItemsButton":
            window = OrderItemsWindow.OrderItemsWindow(self.mysql_cred, self)
        elif pressed == "OrdersButton":
            window = OrdersWindow.OrdersWindow(self.mysql_cred, self)
        # Open the selected window
        window.show()


# endregion Code
