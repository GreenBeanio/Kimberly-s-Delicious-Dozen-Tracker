# Form implementation generated from reading ui file 'UI_RAW\Orders.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OrdersDialog(object):
    def setupUi(self, OrdersDialog):
        OrdersDialog.setObjectName("OrdersDialog")
        OrdersDialog.resize(1131, 963)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_RAW\\../UI/KDD Icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        OrdersDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(OrdersDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.SelectionGrid = QtWidgets.QGridLayout()
        self.SelectionGrid.setObjectName("SelectionGrid")
        self.PlannedDate = QtWidgets.QDateEdit(parent=OrdersDialog)
        self.PlannedDate.setObjectName("PlannedDate")
        self.SelectionGrid.addWidget(self.PlannedDate, 3, 2, 1, 1)
        self.GetPlannedDateButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.GetPlannedDateButton.setObjectName("GetPlannedDateButton")
        self.SelectionGrid.addWidget(self.GetPlannedDateButton, 3, 3, 1, 1)
        self.GetFinalDateButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.GetFinalDateButton.setObjectName("GetFinalDateButton")
        self.SelectionGrid.addWidget(self.GetFinalDateButton, 4, 3, 1, 1)
        self.PlannedLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.PlannedLabel.setObjectName("PlannedLabel")
        self.SelectionGrid.addWidget(self.PlannedLabel, 3, 0, 1, 1)
        self.OrderDate = QtWidgets.QDateEdit(parent=OrdersDialog)
        self.OrderDate.setObjectName("OrderDate")
        self.SelectionGrid.addWidget(self.OrderDate, 2, 2, 1, 1)
        self.FinalDate = QtWidgets.QDateEdit(parent=OrdersDialog)
        self.FinalDate.setObjectName("FinalDate")
        self.SelectionGrid.addWidget(self.FinalDate, 4, 2, 1, 1)
        self.OrderLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.OrderLabel.setObjectName("OrderLabel")
        self.SelectionGrid.addWidget(self.OrderLabel, 0, 0, 1, 1)
        self.FinalLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.FinalLabel.setObjectName("FinalLabel")
        self.SelectionGrid.addWidget(self.FinalLabel, 4, 0, 1, 1)
        self.OrderText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.OrderText.setObjectName("OrderText")
        self.SelectionGrid.addWidget(self.OrderText, 0, 2, 1, 1)
        self.NoteText = QtWidgets.QTextEdit(parent=OrdersDialog)
        self.NoteText.setObjectName("NoteText")
        self.SelectionGrid.addWidget(self.NoteText, 8, 2, 1, 1)
        self.CustomerLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.CustomerLabel.setObjectName("CustomerLabel")
        self.SelectionGrid.addWidget(self.CustomerLabel, 1, 0, 1, 1)
        self.CustomerText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.CustomerText.setObjectName("CustomerText")
        self.SelectionGrid.addWidget(self.CustomerText, 1, 2, 1, 1)
        self.OrderLabel_2 = QtWidgets.QLabel(parent=OrdersDialog)
        self.OrderLabel_2.setObjectName("OrderLabel_2")
        self.SelectionGrid.addWidget(self.OrderLabel_2, 2, 0, 1, 1)
        self.PriceText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.PriceText.setObjectName("PriceText")
        self.SelectionGrid.addWidget(self.PriceText, 5, 2, 1, 1)
        self.StatusLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.StatusLabel.setObjectName("StatusLabel")
        self.SelectionGrid.addWidget(self.StatusLabel, 6, 0, 1, 1)
        self.PriceLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.PriceLabel.setObjectName("PriceLabel")
        self.SelectionGrid.addWidget(self.PriceLabel, 5, 0, 1, 1)
        self.CustomersButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.CustomersButton.setObjectName("CustomersButton")
        self.SelectionGrid.addWidget(self.CustomersButton, 1, 3, 1, 1)
        self.OrderNote = QtWidgets.QLabel(parent=OrdersDialog)
        self.OrderNote.setObjectName("OrderNote")
        self.SelectionGrid.addWidget(self.OrderNote, 8, 0, 1, 1)
        self.GetOrderDateButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.GetOrderDateButton.setObjectName("GetOrderDateButton")
        self.SelectionGrid.addWidget(self.GetOrderDateButton, 2, 3, 1, 1)
        self.StatusBox = QtWidgets.QComboBox(parent=OrdersDialog)
        self.StatusBox.setObjectName("StatusBox")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.SelectionGrid.addWidget(self.StatusBox, 6, 2, 1, 1)
        self.ResetButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.ResetButton.setObjectName("ResetButton")
        self.SelectionGrid.addWidget(self.ResetButton, 4, 4, 1, 1)
        self.PaymentLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.PaymentLabel.setObjectName("PaymentLabel")
        self.SelectionGrid.addWidget(self.PaymentLabel, 7, 0, 1, 1)
        self.PaymentText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.PaymentText.setObjectName("PaymentText")
        self.SelectionGrid.addWidget(self.PaymentText, 7, 2, 1, 1)
        self.CalculatePrice = QtWidgets.QPushButton(parent=OrdersDialog)
        self.CalculatePrice.setObjectName("CalculatePrice")
        self.SelectionGrid.addWidget(self.CalculatePrice, 5, 3, 1, 1)
        self.InputLayout.addLayout(self.SelectionGrid)
        self.MainLayout.addLayout(self.InputLayout)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.ModificationLayout = QtWidgets.QHBoxLayout()
        self.ModificationLayout.setObjectName("ModificationLayout")
        self.AddButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.AddButton.setObjectName("AddButton")
        self.ModificationLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.UpdateButton.setObjectName("UpdateButton")
        self.ModificationLayout.addWidget(self.UpdateButton)
        self.DeleteButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ModificationLayout.addWidget(self.DeleteButton)
        self.OutputLayout.addLayout(self.ModificationLayout)
        self.SearchLayout = QtWidgets.QGridLayout()
        self.SearchLayout.setObjectName("SearchLayout")
        self.DateSelectionSection = QtWidgets.QGridLayout()
        self.DateSelectionSection.setObjectName("DateSelectionSection")
        self.StartDateLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.StartDateLabel.setObjectName("StartDateLabel")
        self.DateSelectionSection.addWidget(self.StartDateLabel, 1, 0, 1, 1)
        self.EndDateLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.EndDateLabel.setObjectName("EndDateLabel")
        self.DateSelectionSection.addWidget(self.EndDateLabel, 2, 0, 1, 1)
        self.DateTypeLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.DateTypeLabel.setObjectName("DateTypeLabel")
        self.DateSelectionSection.addWidget(self.DateTypeLabel, 0, 0, 1, 1)
        self.StartDateSelect = QtWidgets.QDateEdit(parent=OrdersDialog)
        self.StartDateSelect.setObjectName("StartDateSelect")
        self.DateSelectionSection.addWidget(self.StartDateSelect, 1, 1, 1, 1)
        self.EndDateSelect = QtWidgets.QDateEdit(parent=OrdersDialog)
        self.EndDateSelect.setObjectName("EndDateSelect")
        self.DateSelectionSection.addWidget(self.EndDateSelect, 2, 1, 1, 1)
        self.DateTypeBox = QtWidgets.QComboBox(parent=OrdersDialog)
        self.DateTypeBox.setObjectName("DateTypeBox")
        self.DateTypeBox.addItem("")
        self.DateTypeBox.addItem("")
        self.DateTypeBox.addItem("")
        self.DateSelectionSection.addWidget(self.DateTypeBox, 0, 1, 1, 1)
        self.EnableDate = QtWidgets.QCheckBox(parent=OrdersDialog)
        self.EnableDate.setText("")
        self.EnableDate.setObjectName("EnableDate")
        self.DateSelectionSection.addWidget(self.EnableDate, 0, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.GetStartDate = QtWidgets.QPushButton(parent=OrdersDialog)
        self.GetStartDate.setObjectName("GetStartDate")
        self.DateSelectionSection.addWidget(self.GetStartDate, 1, 4, 1, 1)
        self.GetEndDate = QtWidgets.QPushButton(parent=OrdersDialog)
        self.GetEndDate.setObjectName("GetEndDate")
        self.DateSelectionSection.addWidget(self.GetEndDate, 2, 4, 1, 1)
        self.DateSelectionSection.setColumnStretch(1, 1)
        self.SearchLayout.addLayout(self.DateSelectionSection, 2, 0, 1, 1)
        self.SearchContainer = QtWidgets.QVBoxLayout()
        self.SearchContainer.setObjectName("SearchContainer")
        self.SearchSection = QtWidgets.QGridLayout()
        self.SearchSection.setObjectName("SearchSection")
        self.StatusSearchLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.StatusSearchLabel.setObjectName("StatusSearchLabel")
        self.SearchSection.addWidget(self.StatusSearchLabel, 3, 0, 1, 1)
        self.OrderSearchLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.OrderSearchLabel.setObjectName("OrderSearchLabel")
        self.SearchSection.addWidget(self.OrderSearchLabel, 1, 0, 1, 1)
        self.CustomerSearchText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.CustomerSearchText.setObjectName("CustomerSearchText")
        self.SearchSection.addWidget(self.CustomerSearchText, 2, 2, 1, 1)
        self.StatusComboSearch = QtWidgets.QComboBox(parent=OrdersDialog)
        self.StatusComboSearch.setMaxCount(2147483647)
        self.StatusComboSearch.setObjectName("StatusComboSearch")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.SearchSection.addWidget(self.StatusComboSearch, 3, 2, 1, 1)
        self.StatusEnable = QtWidgets.QCheckBox(parent=OrdersDialog)
        self.StatusEnable.setText("")
        self.StatusEnable.setObjectName("StatusEnable")
        self.SearchSection.addWidget(self.StatusEnable, 3, 3, 1, 1)
        self.CustomerEnable = QtWidgets.QCheckBox(parent=OrdersDialog)
        self.CustomerEnable.setText("")
        self.CustomerEnable.setObjectName("CustomerEnable")
        self.SearchSection.addWidget(self.CustomerEnable, 2, 3, 1, 1)
        self.OrderSearchText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.OrderSearchText.setObjectName("OrderSearchText")
        self.SearchSection.addWidget(self.OrderSearchText, 1, 2, 1, 1)
        self.OrderEnable = QtWidgets.QCheckBox(parent=OrdersDialog)
        self.OrderEnable.setText("")
        self.OrderEnable.setObjectName("OrderEnable")
        self.SearchSection.addWidget(self.OrderEnable, 1, 3, 1, 1)
        self.CustomerSearchLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.CustomerSearchLabel.setObjectName("CustomerSearchLabel")
        self.SearchSection.addWidget(self.CustomerSearchLabel, 2, 0, 1, 1)
        self.SearchContainer.addLayout(self.SearchSection)
        self.SearchLayout.addLayout(self.SearchContainer, 1, 0, 1, 1)
        self.SearchSectionLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.SearchSectionLabel.setObjectName("SearchSectionLabel")
        self.SearchLayout.addWidget(self.SearchSectionLabel, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.CalculateContainer = QtWidgets.QVBoxLayout()
        self.CalculateContainer.setObjectName("CalculateContainer")
        self.CalculateLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.CalculateLabel.setObjectName("CalculateLabel")
        self.CalculateContainer.addWidget(self.CalculateLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.CalculateSelection = QtWidgets.QHBoxLayout()
        self.CalculateSelection.setObjectName("CalculateSelection")
        self.TotalSalesLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.TotalSalesLabel.setObjectName("TotalSalesLabel")
        self.CalculateSelection.addWidget(self.TotalSalesLabel)
        self.TotalSales = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.TotalSales.setReadOnly(True)
        self.TotalSales.setObjectName("TotalSales")
        self.CalculateSelection.addWidget(self.TotalSales)
        self.GetTotalSales = QtWidgets.QPushButton(parent=OrdersDialog)
        self.GetTotalSales.setObjectName("GetTotalSales")
        self.CalculateSelection.addWidget(self.GetTotalSales)
        self.CalculateContainer.addLayout(self.CalculateSelection)
        self.SearchLayout.addLayout(self.CalculateContainer, 3, 0, 1, 1)
        self.OutputLayout.addLayout(self.SearchLayout)
        self.ResultLayout = QtWidgets.QHBoxLayout()
        self.ResultLayout.setObjectName("ResultLayout")
        self.OutputLabel = QtWidgets.QLabel(parent=OrdersDialog)
        self.OutputLabel.setObjectName("OutputLabel")
        self.ResultLayout.addWidget(self.OutputLabel)
        self.OutputText = QtWidgets.QLineEdit(parent=OrdersDialog)
        self.OutputText.setReadOnly(True)
        self.OutputText.setObjectName("OutputText")
        self.ResultLayout.addWidget(self.OutputText)
        self.OutputLayout.addLayout(self.ResultLayout)
        self.MainLayout.addLayout(self.OutputLayout)
        self.OrderTable = QtWidgets.QTableView(parent=OrdersDialog)
        self.OrderTable.setSortingEnabled(False)
        self.OrderTable.setObjectName("OrderTable")
        self.MainLayout.addWidget(self.OrderTable)
        self.BottomButtons = QtWidgets.QHBoxLayout()
        self.BottomButtons.setObjectName("BottomButtons")
        self.Reload = QtWidgets.QPushButton(parent=OrdersDialog)
        self.Reload.setObjectName("Reload")
        self.BottomButtons.addWidget(self.Reload)
        self.ShowOrderItemsButton = QtWidgets.QPushButton(parent=OrdersDialog)
        self.ShowOrderItemsButton.setObjectName("ShowOrderItemsButton")
        self.BottomButtons.addWidget(self.ShowOrderItemsButton)
        self.UpdateEmptyPrices = QtWidgets.QPushButton(parent=OrdersDialog)
        self.UpdateEmptyPrices.setObjectName("UpdateEmptyPrices")
        self.BottomButtons.addWidget(self.UpdateEmptyPrices)
        self.BottomButtons.setStretch(0, 1)
        self.MainLayout.addLayout(self.BottomButtons)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(2, 4)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)

        self.retranslateUi(OrdersDialog)
        QtCore.QMetaObject.connectSlotsByName(OrdersDialog)
        OrdersDialog.setTabOrder(self.OrderText, self.CustomerText)
        OrdersDialog.setTabOrder(self.CustomerText, self.CustomersButton)
        OrdersDialog.setTabOrder(self.CustomersButton, self.OrderDate)
        OrdersDialog.setTabOrder(self.OrderDate, self.GetOrderDateButton)
        OrdersDialog.setTabOrder(self.GetOrderDateButton, self.PlannedDate)
        OrdersDialog.setTabOrder(self.PlannedDate, self.FinalDate)
        OrdersDialog.setTabOrder(self.FinalDate, self.PriceText)
        OrdersDialog.setTabOrder(self.PriceText, self.StatusBox)
        OrdersDialog.setTabOrder(self.StatusBox, self.NoteText)
        OrdersDialog.setTabOrder(self.NoteText, self.AddButton)
        OrdersDialog.setTabOrder(self.AddButton, self.UpdateButton)
        OrdersDialog.setTabOrder(self.UpdateButton, self.DeleteButton)
        OrdersDialog.setTabOrder(self.DeleteButton, self.OutputText)
        OrdersDialog.setTabOrder(self.OutputText, self.OrderTable)

    def retranslateUi(self, OrdersDialog):
        _translate = QtCore.QCoreApplication.translate
        OrdersDialog.setWindowTitle(_translate("OrdersDialog", "Orders"))
        self.GetPlannedDateButton.setText(_translate("OrdersDialog", "Get Date"))
        self.GetFinalDateButton.setText(_translate("OrdersDialog", "Get Date"))
        self.PlannedLabel.setText(_translate("OrdersDialog", "Planned Date:"))
        self.OrderLabel.setText(_translate("OrdersDialog", "Order Name:"))
        self.FinalLabel.setText(_translate("OrdersDialog", "Final Date:"))
        self.CustomerLabel.setText(_translate("OrdersDialog", "Customer:"))
        self.OrderLabel_2.setText(_translate("OrdersDialog", "Order Date:"))
        self.StatusLabel.setText(_translate("OrdersDialog", "Status:"))
        self.PriceLabel.setText(_translate("OrdersDialog", "Price:"))
        self.CustomersButton.setText(_translate("OrdersDialog", "Show Customers"))
        self.OrderNote.setText(_translate("OrdersDialog", "Note:"))
        self.GetOrderDateButton.setText(_translate("OrdersDialog", "Get Date"))
        self.StatusBox.setItemText(0, _translate("OrdersDialog", "Production"))
        self.StatusBox.setItemText(1, _translate("OrdersDialog", "Sold"))
        self.StatusBox.setItemText(2, _translate("OrdersDialog", "Cancelled"))
        self.StatusBox.setItemText(3, _translate("OrdersDialog", "Preorder"))
        self.StatusBox.setItemText(4, _translate("OrdersDialog", "No Payment"))
        self.StatusBox.setItemText(5, _translate("OrdersDialog", "Late"))
        self.ResetButton.setText(_translate("OrdersDialog", "Reset"))
        self.PaymentLabel.setText(_translate("OrdersDialog", "Payment Type:"))
        self.CalculatePrice.setText(_translate("OrdersDialog", "Calculate Price"))
        self.AddButton.setText(_translate("OrdersDialog", "Add"))
        self.UpdateButton.setText(_translate("OrdersDialog", "Update"))
        self.DeleteButton.setText(_translate("OrdersDialog", "Delete"))
        self.StartDateLabel.setText(_translate("OrdersDialog", "Start Date:"))
        self.EndDateLabel.setText(_translate("OrdersDialog", "End Date:"))
        self.DateTypeLabel.setText(_translate("OrdersDialog", "Date Type:"))
        self.DateTypeBox.setItemText(0, _translate("OrdersDialog", "Order Date"))
        self.DateTypeBox.setItemText(1, _translate("OrdersDialog", "Planned Date"))
        self.DateTypeBox.setItemText(2, _translate("OrdersDialog", "Final Date"))
        self.GetStartDate.setText(_translate("OrdersDialog", "Get Date"))
        self.GetEndDate.setText(_translate("OrdersDialog", "Get Date"))
        self.StatusSearchLabel.setText(_translate("OrdersDialog", "Status:"))
        self.OrderSearchLabel.setText(_translate("OrdersDialog", "Order:"))
        self.StatusComboSearch.setItemText(0, _translate("OrdersDialog", "Production"))
        self.StatusComboSearch.setItemText(1, _translate("OrdersDialog", "Sold"))
        self.StatusComboSearch.setItemText(2, _translate("OrdersDialog", "Cancelled"))
        self.StatusComboSearch.setItemText(3, _translate("OrdersDialog", "Preorder"))
        self.StatusComboSearch.setItemText(4, _translate("OrdersDialog", "No Payment"))
        self.StatusComboSearch.setItemText(5, _translate("OrdersDialog", "Late"))
        self.CustomerSearchLabel.setText(_translate("OrdersDialog", "Customer:"))
        self.SearchSectionLabel.setText(_translate("OrdersDialog", "Search Options"))
        self.CalculateLabel.setText(_translate("OrdersDialog", "Calculate"))
        self.TotalSalesLabel.setText(_translate("OrdersDialog", "Total Sales:"))
        self.GetTotalSales.setText(_translate("OrdersDialog", "Get Total Sales"))
        self.OutputLabel.setText(_translate("OrdersDialog", "Result:"))
        self.Reload.setText(_translate("OrdersDialog", "Reload"))
        self.ShowOrderItemsButton.setText(_translate("OrdersDialog", "Show Order Items"))
        self.UpdateEmptyPrices.setText(_translate("OrdersDialog", "Update Empty Prices"))
