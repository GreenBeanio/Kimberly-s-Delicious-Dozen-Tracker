# Form implementation generated from reading ui file '.\UI_RAW\Main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(263, 122)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=MainDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ActivitiesButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.ActivitiesButton.setObjectName("ActivitiesButton")
        self.gridLayout.addWidget(self.ActivitiesButton, 1, 0, 1, 1)
        self.LogButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.LogButton.setObjectName("LogButton")
        self.gridLayout.addWidget(self.LogButton, 0, 0, 1, 1)
        self.ItemsButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.ItemsButton.setObjectName("ItemsButton")
        self.gridLayout.addWidget(self.ItemsButton, 2, 0, 1, 1)
        self.CustomersButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.CustomersButton.setObjectName("CustomersButton")
        self.gridLayout.addWidget(self.CustomersButton, 0, 1, 1, 1)
        self.OrdersButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.OrdersButton.setObjectName("OrdersButton")
        self.gridLayout.addWidget(self.OrdersButton, 1, 1, 1, 1)
        self.OrderItemsButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.OrderItemsButton.setObjectName("OrderItemsButton")
        self.gridLayout.addWidget(self.OrderItemsButton, 2, 1, 1, 1)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)
        MainDialog.setTabOrder(self.LogButton, self.CustomersButton)
        MainDialog.setTabOrder(self.CustomersButton, self.ActivitiesButton)
        MainDialog.setTabOrder(self.ActivitiesButton, self.OrdersButton)
        MainDialog.setTabOrder(self.OrdersButton, self.ItemsButton)
        MainDialog.setTabOrder(self.ItemsButton, self.OrderItemsButton)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Kimberly\'s Delicious Dozen"))
        self.ActivitiesButton.setText(_translate("MainDialog", "Activities"))
        self.LogButton.setText(_translate("MainDialog", "Log"))
        self.ItemsButton.setText(_translate("MainDialog", "Items"))
        self.CustomersButton.setText(_translate("MainDialog", "Customers"))
        self.OrdersButton.setText(_translate("MainDialog", "Orders"))
        self.OrderItemsButton.setText(_translate("MainDialog", "Order Items"))
