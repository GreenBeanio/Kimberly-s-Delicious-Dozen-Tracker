# Form implementation generated from reading ui file 'UI_RAW\Log.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        LogDialog.setObjectName("LogDialog")
        LogDialog.resize(964, 764)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_RAW\\../UI/KDD Icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LogDialog.setWindowIcon(icon)
        LogDialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(LogDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.SelectionGrid = QtWidgets.QGridLayout()
        self.SelectionGrid.setObjectName("SelectionGrid")
        self.ShowOrdersButton = QtWidgets.QPushButton(parent=LogDialog)
        self.ShowOrdersButton.setObjectName("ShowOrdersButton")
        self.SelectionGrid.addWidget(self.ShowOrdersButton, 4, 2, 1, 1)
        self.ActivitiesText = QtWidgets.QLineEdit(parent=LogDialog)
        self.ActivitiesText.setObjectName("ActivitiesText")
        self.SelectionGrid.addWidget(self.ActivitiesText, 3, 1, 1, 1)
        self.ActivityLabel = QtWidgets.QLabel(parent=LogDialog)
        self.ActivityLabel.setObjectName("ActivityLabel")
        self.SelectionGrid.addWidget(self.ActivityLabel, 3, 0, 1, 1)
        self.GetStartButton = QtWidgets.QPushButton(parent=LogDialog)
        self.GetStartButton.setObjectName("GetStartButton")
        self.SelectionGrid.addWidget(self.GetStartButton, 1, 2, 1, 1)
        self.StartSelect = QtWidgets.QTimeEdit(parent=LogDialog)
        self.StartSelect.setObjectName("StartSelect")
        self.SelectionGrid.addWidget(self.StartSelect, 1, 1, 1, 1)
        self.EndLabel = QtWidgets.QLabel(parent=LogDialog)
        self.EndLabel.setObjectName("EndLabel")
        self.SelectionGrid.addWidget(self.EndLabel, 2, 0, 1, 1)
        self.ShowActivitiesButton = QtWidgets.QPushButton(parent=LogDialog)
        self.ShowActivitiesButton.setObjectName("ShowActivitiesButton")
        self.SelectionGrid.addWidget(self.ShowActivitiesButton, 3, 2, 1, 1)
        self.GetDateButton = QtWidgets.QPushButton(parent=LogDialog)
        self.GetDateButton.setObjectName("GetDateButton")
        self.SelectionGrid.addWidget(self.GetDateButton, 0, 2, 1, 1)
        self.OrderLabel = QtWidgets.QLabel(parent=LogDialog)
        self.OrderLabel.setObjectName("OrderLabel")
        self.SelectionGrid.addWidget(self.OrderLabel, 4, 0, 1, 1)
        self.StartLabel = QtWidgets.QLabel(parent=LogDialog)
        self.StartLabel.setObjectName("StartLabel")
        self.SelectionGrid.addWidget(self.StartLabel, 1, 0, 1, 1)
        self.EndSelect = QtWidgets.QTimeEdit(parent=LogDialog)
        self.EndSelect.setObjectName("EndSelect")
        self.SelectionGrid.addWidget(self.EndSelect, 2, 1, 1, 1)
        self.DateLabel = QtWidgets.QLabel(parent=LogDialog)
        self.DateLabel.setObjectName("DateLabel")
        self.SelectionGrid.addWidget(self.DateLabel, 0, 0, 1, 1)
        self.GetEndButton = QtWidgets.QPushButton(parent=LogDialog)
        self.GetEndButton.setObjectName("GetEndButton")
        self.SelectionGrid.addWidget(self.GetEndButton, 2, 2, 1, 1)
        self.DataSelect = QtWidgets.QDateEdit(parent=LogDialog)
        self.DataSelect.setObjectName("DataSelect")
        self.SelectionGrid.addWidget(self.DataSelect, 0, 1, 1, 1)
        self.OrderText = QtWidgets.QLineEdit(parent=LogDialog)
        self.OrderText.setObjectName("OrderText")
        self.SelectionGrid.addWidget(self.OrderText, 4, 1, 1, 1)
        self.InputLayout.addLayout(self.SelectionGrid)
        self.NoteLayout = QtWidgets.QVBoxLayout()
        self.NoteLayout.setObjectName("NoteLayout")
        self.NoteLabel = QtWidgets.QLabel(parent=LogDialog)
        self.NoteLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.NoteLabel.setWordWrap(False)
        self.NoteLabel.setObjectName("NoteLabel")
        self.NoteLayout.addWidget(self.NoteLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.NoteBox = QtWidgets.QTextEdit(parent=LogDialog)
        self.NoteBox.setObjectName("NoteBox")
        self.NoteLayout.addWidget(self.NoteBox)
        self.InputLayout.addLayout(self.NoteLayout)
        self.MainLayout.addLayout(self.InputLayout)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.ModificationLayout = QtWidgets.QHBoxLayout()
        self.ModificationLayout.setObjectName("ModificationLayout")
        self.AddButton = QtWidgets.QPushButton(parent=LogDialog)
        self.AddButton.setObjectName("AddButton")
        self.ModificationLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(parent=LogDialog)
        self.UpdateButton.setObjectName("UpdateButton")
        self.ModificationLayout.addWidget(self.UpdateButton)
        self.DeleteButton = QtWidgets.QPushButton(parent=LogDialog)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ModificationLayout.addWidget(self.DeleteButton)
        self.OutputLayout.addLayout(self.ModificationLayout)
        self.SearchSection = QtWidgets.QGridLayout()
        self.SearchSection.setObjectName("SearchSection")
        self.SearchLabel = QtWidgets.QLabel(parent=LogDialog)
        self.SearchLabel.setObjectName("SearchLabel")
        self.SearchSection.addWidget(self.SearchLabel, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.SearchContainer = QtWidgets.QVBoxLayout()
        self.SearchContainer.setObjectName("SearchContainer")
        self.SearchGrid = QtWidgets.QGridLayout()
        self.SearchGrid.setObjectName("SearchGrid")
        self.EnableOrder = QtWidgets.QCheckBox(parent=LogDialog)
        self.EnableOrder.setText("")
        self.EnableOrder.setObjectName("EnableOrder")
        self.SearchGrid.addWidget(self.EnableOrder, 0, 2, 1, 1)
        self.EnableActivity = QtWidgets.QCheckBox(parent=LogDialog)
        self.EnableActivity.setText("")
        self.EnableActivity.setObjectName("EnableActivity")
        self.SearchGrid.addWidget(self.EnableActivity, 1, 2, 1, 1)
        self.ActivitySearchLabel = QtWidgets.QLabel(parent=LogDialog)
        self.ActivitySearchLabel.setObjectName("ActivitySearchLabel")
        self.SearchGrid.addWidget(self.ActivitySearchLabel, 1, 0, 1, 1)
        self.OrderSearchLabel = QtWidgets.QLabel(parent=LogDialog)
        self.OrderSearchLabel.setObjectName("OrderSearchLabel")
        self.SearchGrid.addWidget(self.OrderSearchLabel, 0, 0, 1, 1)
        self.ActivitySearch = QtWidgets.QLineEdit(parent=LogDialog)
        self.ActivitySearch.setObjectName("ActivitySearch")
        self.SearchGrid.addWidget(self.ActivitySearch, 1, 1, 1, 1)
        self.OrderSearch = QtWidgets.QLineEdit(parent=LogDialog)
        self.OrderSearch.setObjectName("OrderSearch")
        self.SearchGrid.addWidget(self.OrderSearch, 0, 1, 1, 1)
        self.SearchContainer.addLayout(self.SearchGrid)
        self.DateGrid = QtWidgets.QGridLayout()
        self.DateGrid.setObjectName("DateGrid")
        self.GetDateEndDate = QtWidgets.QPushButton(parent=LogDialog)
        self.GetDateEndDate.setObjectName("GetDateEndDate")
        self.DateGrid.addWidget(self.GetDateEndDate, 1, 2, 1, 1)
        self.StartDate = QtWidgets.QDateEdit(parent=LogDialog)
        self.StartDate.setObjectName("StartDate")
        self.DateGrid.addWidget(self.StartDate, 0, 1, 1, 1)
        self.EndDateLabel = QtWidgets.QLabel(parent=LogDialog)
        self.EndDateLabel.setObjectName("EndDateLabel")
        self.DateGrid.addWidget(self.EndDateLabel, 1, 0, 1, 1)
        self.EndDate = QtWidgets.QDateEdit(parent=LogDialog)
        self.EndDate.setObjectName("EndDate")
        self.DateGrid.addWidget(self.EndDate, 1, 1, 1, 1)
        self.StartDateLabel = QtWidgets.QLabel(parent=LogDialog)
        self.StartDateLabel.setObjectName("StartDateLabel")
        self.DateGrid.addWidget(self.StartDateLabel, 0, 0, 1, 1)
        self.GetDateStartDate = QtWidgets.QPushButton(parent=LogDialog)
        self.GetDateStartDate.setObjectName("GetDateStartDate")
        self.DateGrid.addWidget(self.GetDateStartDate, 0, 2, 1, 1)
        self.EnableStart = QtWidgets.QCheckBox(parent=LogDialog)
        self.EnableStart.setText("")
        self.EnableStart.setObjectName("EnableStart")
        self.DateGrid.addWidget(self.EnableStart, 0, 3, 1, 1)
        self.EnableEnd = QtWidgets.QCheckBox(parent=LogDialog)
        self.EnableEnd.setText("")
        self.EnableEnd.setObjectName("EnableEnd")
        self.DateGrid.addWidget(self.EnableEnd, 1, 3, 1, 1)
        self.DateGrid.setColumnStretch(1, 1)
        self.SearchContainer.addLayout(self.DateGrid)
        self.SearchSection.addLayout(self.SearchContainer, 1, 0, 1, 1)
        self.OutputLayout.addLayout(self.SearchSection)
        self.CalculateSeciton = QtWidgets.QVBoxLayout()
        self.CalculateSeciton.setObjectName("CalculateSeciton")
        self.CalculateLabel = QtWidgets.QLabel(parent=LogDialog)
        self.CalculateLabel.setObjectName("CalculateLabel")
        self.CalculateSeciton.addWidget(self.CalculateLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.CalculateContainer = QtWidgets.QHBoxLayout()
        self.CalculateContainer.setObjectName("CalculateContainer")
        self.CalculateTimeLabel = QtWidgets.QLabel(parent=LogDialog)
        self.CalculateTimeLabel.setObjectName("CalculateTimeLabel")
        self.CalculateContainer.addWidget(self.CalculateTimeLabel)
        self.TotalHours = QtWidgets.QLineEdit(parent=LogDialog)
        self.TotalHours.setEnabled(True)
        self.TotalHours.setReadOnly(True)
        self.TotalHours.setObjectName("TotalHours")
        self.CalculateContainer.addWidget(self.TotalHours)
        self.GetTotalHours = QtWidgets.QPushButton(parent=LogDialog)
        self.GetTotalHours.setObjectName("GetTotalHours")
        self.CalculateContainer.addWidget(self.GetTotalHours)
        self.CalculateSeciton.addLayout(self.CalculateContainer)
        self.OutputLayout.addLayout(self.CalculateSeciton)
        self.ResultLayout = QtWidgets.QHBoxLayout()
        self.ResultLayout.setObjectName("ResultLayout")
        self.OutputLabel = QtWidgets.QLabel(parent=LogDialog)
        self.OutputLabel.setObjectName("OutputLabel")
        self.ResultLayout.addWidget(self.OutputLabel)
        self.OutputText = QtWidgets.QLineEdit(parent=LogDialog)
        self.OutputText.setReadOnly(True)
        self.OutputText.setObjectName("OutputText")
        self.ResultLayout.addWidget(self.OutputText)
        self.OutputLayout.addLayout(self.ResultLayout)
        self.MainLayout.addLayout(self.OutputLayout)
        self.LogTable = QtWidgets.QTableView(parent=LogDialog)
        self.LogTable.setObjectName("LogTable")
        self.MainLayout.addWidget(self.LogTable)
        self.Reload = QtWidgets.QPushButton(parent=LogDialog)
        self.Reload.setObjectName("Reload")
        self.MainLayout.addWidget(self.Reload)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(2, 4)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)

        self.retranslateUi(LogDialog)
        QtCore.QMetaObject.connectSlotsByName(LogDialog)
        LogDialog.setTabOrder(self.DataSelect, self.GetDateButton)
        LogDialog.setTabOrder(self.GetDateButton, self.StartSelect)
        LogDialog.setTabOrder(self.StartSelect, self.GetStartButton)
        LogDialog.setTabOrder(self.GetStartButton, self.EndSelect)
        LogDialog.setTabOrder(self.EndSelect, self.GetEndButton)
        LogDialog.setTabOrder(self.GetEndButton, self.ShowActivitiesButton)
        LogDialog.setTabOrder(self.ShowActivitiesButton, self.ShowOrdersButton)
        LogDialog.setTabOrder(self.ShowOrdersButton, self.NoteBox)
        LogDialog.setTabOrder(self.NoteBox, self.AddButton)
        LogDialog.setTabOrder(self.AddButton, self.UpdateButton)
        LogDialog.setTabOrder(self.UpdateButton, self.DeleteButton)
        LogDialog.setTabOrder(self.DeleteButton, self.OutputText)
        LogDialog.setTabOrder(self.OutputText, self.LogTable)

    def retranslateUi(self, LogDialog):
        _translate = QtCore.QCoreApplication.translate
        LogDialog.setWindowTitle(_translate("LogDialog", "Log"))
        self.ShowOrdersButton.setText(_translate("LogDialog", "Show Orders"))
        self.ActivityLabel.setText(_translate("LogDialog", "Activity:"))
        self.GetStartButton.setText(_translate("LogDialog", "Get Time"))
        self.StartSelect.setDisplayFormat(_translate("LogDialog", "hh:mm AP"))
        self.EndLabel.setText(_translate("LogDialog", "End:"))
        self.ShowActivitiesButton.setText(_translate("LogDialog", "Show Activities"))
        self.GetDateButton.setText(_translate("LogDialog", "Get Date"))
        self.OrderLabel.setText(_translate("LogDialog", "Order:"))
        self.StartLabel.setText(_translate("LogDialog", "Start:"))
        self.EndSelect.setDisplayFormat(_translate("LogDialog", "hh:mm AP"))
        self.DateLabel.setText(_translate("LogDialog", "Date:"))
        self.GetEndButton.setText(_translate("LogDialog", "Get Time"))
        self.NoteLabel.setText(_translate("LogDialog", "Note:"))
        self.AddButton.setText(_translate("LogDialog", "Add"))
        self.UpdateButton.setText(_translate("LogDialog", "Update"))
        self.DeleteButton.setText(_translate("LogDialog", "Delete"))
        self.SearchLabel.setText(_translate("LogDialog", "Search Options"))
        self.ActivitySearchLabel.setText(_translate("LogDialog", "Activity:"))
        self.OrderSearchLabel.setText(_translate("LogDialog", "Order:"))
        self.GetDateEndDate.setText(_translate("LogDialog", "Get Date"))
        self.EndDateLabel.setText(_translate("LogDialog", "End Date:"))
        self.StartDateLabel.setText(_translate("LogDialog", "Start Date:"))
        self.GetDateStartDate.setText(_translate("LogDialog", "Get Date"))
        self.CalculateLabel.setText(_translate("LogDialog", "Calculate"))
        self.CalculateTimeLabel.setText(_translate("LogDialog", "Total Hours:"))
        self.GetTotalHours.setText(_translate("LogDialog", "Get Total Hours"))
        self.OutputLabel.setText(_translate("LogDialog", "Result:"))
        self.Reload.setText(_translate("LogDialog", "Reload"))
