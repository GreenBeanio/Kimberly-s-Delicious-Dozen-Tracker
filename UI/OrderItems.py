# Form implementation generated from reading ui file 'UI_RAW\OrderItems.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OrderItemsDialog(object):
    def setupUi(self, OrderItemsDialog):
        OrderItemsDialog.setObjectName("OrderItemsDialog")
        OrderItemsDialog.resize(560, 613)
        self.gridLayout = QtWidgets.QGridLayout(OrderItemsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.SelectionGrid = QtWidgets.QGridLayout()
        self.SelectionGrid.setObjectName("SelectionGrid")
        self.OrderLabel = QtWidgets.QLabel(parent=OrderItemsDialog)
        self.OrderLabel.setObjectName("OrderLabel")
        self.SelectionGrid.addWidget(self.OrderLabel, 0, 0, 1, 1)
        self.OrdersButton = QtWidgets.QPushButton(parent=OrderItemsDialog)
        self.OrdersButton.setObjectName("OrdersButton")
        self.SelectionGrid.addWidget(self.OrdersButton, 0, 3, 1, 1)
        self.NoteText = QtWidgets.QTextEdit(parent=OrderItemsDialog)
        self.NoteText.setObjectName("NoteText")
        self.SelectionGrid.addWidget(self.NoteText, 4, 2, 1, 1)
        self.ItemsButton = QtWidgets.QPushButton(parent=OrderItemsDialog)
        self.ItemsButton.setObjectName("ItemsButton")
        self.SelectionGrid.addWidget(self.ItemsButton, 1, 3, 1, 1)
        self.ItemLabel = QtWidgets.QLabel(parent=OrderItemsDialog)
        self.ItemLabel.setObjectName("ItemLabel")
        self.SelectionGrid.addWidget(self.ItemLabel, 1, 0, 1, 1)
        self.QuantityText = QtWidgets.QLineEdit(parent=OrderItemsDialog)
        self.QuantityText.setObjectName("QuantityText")
        self.SelectionGrid.addWidget(self.QuantityText, 2, 2, 1, 1)
        self.PriceLabel = QtWidgets.QLabel(parent=OrderItemsDialog)
        self.PriceLabel.setObjectName("PriceLabel")
        self.SelectionGrid.addWidget(self.PriceLabel, 3, 0, 1, 1)
        self.ItemText = QtWidgets.QLineEdit(parent=OrderItemsDialog)
        self.ItemText.setObjectName("ItemText")
        self.SelectionGrid.addWidget(self.ItemText, 1, 2, 1, 1)
        self.NoteLabel = QtWidgets.QLabel(parent=OrderItemsDialog)
        self.NoteLabel.setObjectName("NoteLabel")
        self.SelectionGrid.addWidget(self.NoteLabel, 4, 0, 1, 1)
        self.PriceText = QtWidgets.QLineEdit(parent=OrderItemsDialog)
        self.PriceText.setObjectName("PriceText")
        self.SelectionGrid.addWidget(self.PriceText, 3, 2, 1, 1)
        self.OrderText = QtWidgets.QLineEdit(parent=OrderItemsDialog)
        self.OrderText.setObjectName("OrderText")
        self.SelectionGrid.addWidget(self.OrderText, 0, 2, 1, 1)
        self.QuantityLabel = QtWidgets.QLabel(parent=OrderItemsDialog)
        self.QuantityLabel.setObjectName("QuantityLabel")
        self.SelectionGrid.addWidget(self.QuantityLabel, 2, 0, 1, 1)
        self.InputLayout.addLayout(self.SelectionGrid)
        self.MainLayout.addLayout(self.InputLayout)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.ModificationLayout = QtWidgets.QHBoxLayout()
        self.ModificationLayout.setObjectName("ModificationLayout")
        self.AddButton = QtWidgets.QPushButton(parent=OrderItemsDialog)
        self.AddButton.setObjectName("AddButton")
        self.ModificationLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(parent=OrderItemsDialog)
        self.UpdateButton.setObjectName("UpdateButton")
        self.ModificationLayout.addWidget(self.UpdateButton)
        self.DeleteButton = QtWidgets.QPushButton(parent=OrderItemsDialog)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ModificationLayout.addWidget(self.DeleteButton)
        self.OutputLayout.addLayout(self.ModificationLayout)
        self.ResultLayout = QtWidgets.QHBoxLayout()
        self.ResultLayout.setObjectName("ResultLayout")
        self.OutputLabel = QtWidgets.QLabel(parent=OrderItemsDialog)
        self.OutputLabel.setObjectName("OutputLabel")
        self.ResultLayout.addWidget(self.OutputLabel)
        self.OutputText = QtWidgets.QLineEdit(parent=OrderItemsDialog)
        self.OutputText.setReadOnly(True)
        self.OutputText.setObjectName("OutputText")
        self.ResultLayout.addWidget(self.OutputText)
        self.OutputLayout.addLayout(self.ResultLayout)
        self.MainLayout.addLayout(self.OutputLayout)
        self.OrderItemTable = QtWidgets.QTableView(parent=OrderItemsDialog)
        self.OrderItemTable.setObjectName("OrderItemTable")
        self.MainLayout.addWidget(self.OrderItemTable)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(2, 4)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)

        self.retranslateUi(OrderItemsDialog)
        QtCore.QMetaObject.connectSlotsByName(OrderItemsDialog)
        OrderItemsDialog.setTabOrder(self.OrderText, self.OrdersButton)
        OrderItemsDialog.setTabOrder(self.OrdersButton, self.ItemText)
        OrderItemsDialog.setTabOrder(self.ItemText, self.ItemsButton)
        OrderItemsDialog.setTabOrder(self.ItemsButton, self.QuantityText)
        OrderItemsDialog.setTabOrder(self.QuantityText, self.PriceText)
        OrderItemsDialog.setTabOrder(self.PriceText, self.NoteText)
        OrderItemsDialog.setTabOrder(self.NoteText, self.AddButton)
        OrderItemsDialog.setTabOrder(self.AddButton, self.UpdateButton)
        OrderItemsDialog.setTabOrder(self.UpdateButton, self.DeleteButton)
        OrderItemsDialog.setTabOrder(self.DeleteButton, self.OutputText)
        OrderItemsDialog.setTabOrder(self.OutputText, self.OrderItemTable)

    def retranslateUi(self, OrderItemsDialog):
        _translate = QtCore.QCoreApplication.translate
        OrderItemsDialog.setWindowTitle(_translate("OrderItemsDialog", "Order Items"))
        self.OrderLabel.setText(_translate("OrderItemsDialog", "Order Name:"))
        self.OrdersButton.setText(_translate("OrderItemsDialog", "Show Orders"))
        self.ItemsButton.setText(_translate("OrderItemsDialog", "Show Items"))
        self.ItemLabel.setText(_translate("OrderItemsDialog", "Item:"))
        self.PriceLabel.setText(_translate("OrderItemsDialog", "Price:"))
        self.NoteLabel.setText(_translate("OrderItemsDialog", "Note:"))
        self.QuantityLabel.setText(_translate("OrderItemsDialog", "Quantity:"))
        self.AddButton.setText(_translate("OrderItemsDialog", "Add"))
        self.UpdateButton.setText(_translate("OrderItemsDialog", "Update"))
        self.DeleteButton.setText(_translate("OrderItemsDialog", "Delete"))
        self.OutputLabel.setText(_translate("OrderItemsDialog", "Result:"))
