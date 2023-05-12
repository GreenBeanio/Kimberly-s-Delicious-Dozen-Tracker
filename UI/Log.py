# Form implementation generated from reading ui file '.\UI_RAW\Log.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        LogDialog.setObjectName("LogDialog")
        LogDialog.resize(560, 572)
        LogDialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=LogDialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 557, 571))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.MainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.SelectionGrid = QtWidgets.QGridLayout()
        self.SelectionGrid.setObjectName("SelectionGrid")
        self.GetDateButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.GetDateButton.setObjectName("GetDateButton")
        self.SelectionGrid.addWidget(self.GetDateButton, 0, 2, 1, 1)
        self.DateLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.DateLabel.setObjectName("DateLabel")
        self.SelectionGrid.addWidget(self.DateLabel, 0, 0, 1, 1)
        self.ShowActivitiesButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.ShowActivitiesButton.setObjectName("ShowActivitiesButton")
        self.SelectionGrid.addWidget(self.ShowActivitiesButton, 3, 2, 1, 1)
        self.ShowOrdersButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.ShowOrdersButton.setObjectName("ShowOrdersButton")
        self.SelectionGrid.addWidget(self.ShowOrdersButton, 4, 2, 1, 1)
        self.OrderBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_3)
        self.OrderBox.setObjectName("OrderBox")
        self.SelectionGrid.addWidget(self.OrderBox, 4, 1, 1, 1)
        self.EndSelect = QtWidgets.QTimeEdit(parent=self.verticalLayoutWidget_3)
        self.EndSelect.setObjectName("EndSelect")
        self.SelectionGrid.addWidget(self.EndSelect, 2, 1, 1, 1)
        self.DataSelect = QtWidgets.QDateEdit(parent=self.verticalLayoutWidget_3)
        self.DataSelect.setObjectName("DataSelect")
        self.SelectionGrid.addWidget(self.DataSelect, 0, 1, 1, 1)
        self.GetStartButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.GetStartButton.setObjectName("GetStartButton")
        self.SelectionGrid.addWidget(self.GetStartButton, 1, 2, 1, 1)
        self.StartLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.StartLabel.setObjectName("StartLabel")
        self.SelectionGrid.addWidget(self.StartLabel, 1, 0, 1, 1)
        self.StartSelect = QtWidgets.QTimeEdit(parent=self.verticalLayoutWidget_3)
        self.StartSelect.setObjectName("StartSelect")
        self.SelectionGrid.addWidget(self.StartSelect, 1, 1, 1, 1)
        self.EndLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.EndLabel.setObjectName("EndLabel")
        self.SelectionGrid.addWidget(self.EndLabel, 2, 0, 1, 1)
        self.GetEndButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.GetEndButton.setObjectName("GetEndButton")
        self.SelectionGrid.addWidget(self.GetEndButton, 2, 2, 1, 1)
        self.ActivityLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.ActivityLabel.setObjectName("ActivityLabel")
        self.SelectionGrid.addWidget(self.ActivityLabel, 3, 0, 1, 1)
        self.ActivitiesBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_3)
        self.ActivitiesBox.setObjectName("ActivitiesBox")
        self.SelectionGrid.addWidget(self.ActivitiesBox, 3, 1, 1, 1)
        self.OrderLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.OrderLabel.setObjectName("OrderLabel")
        self.SelectionGrid.addWidget(self.OrderLabel, 4, 0, 1, 1)
        self.InputLayout.addLayout(self.SelectionGrid)
        self.NoteLayout = QtWidgets.QVBoxLayout()
        self.NoteLayout.setObjectName("NoteLayout")
        self.NoteLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.NoteLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.NoteLabel.setWordWrap(False)
        self.NoteLabel.setObjectName("NoteLabel")
        self.NoteLayout.addWidget(self.NoteLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.NoteBox = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_3)
        self.NoteBox.setObjectName("NoteBox")
        self.NoteLayout.addWidget(self.NoteBox)
        self.InputLayout.addLayout(self.NoteLayout)
        self.MainLayout.addLayout(self.InputLayout)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.ModificationLayout = QtWidgets.QHBoxLayout()
        self.ModificationLayout.setObjectName("ModificationLayout")
        self.AddButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.AddButton.setObjectName("AddButton")
        self.ModificationLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.UpdateButton.setObjectName("UpdateButton")
        self.ModificationLayout.addWidget(self.UpdateButton)
        self.DeleteButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ModificationLayout.addWidget(self.DeleteButton)
        self.OutputLayout.addLayout(self.ModificationLayout)
        self.ResultLayout = QtWidgets.QHBoxLayout()
        self.ResultLayout.setObjectName("ResultLayout")
        self.OutputLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.OutputLabel.setObjectName("OutputLabel")
        self.ResultLayout.addWidget(self.OutputLabel)
        self.OutputText = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.OutputText.setReadOnly(True)
        self.OutputText.setObjectName("OutputText")
        self.ResultLayout.addWidget(self.OutputText)
        self.OutputLayout.addLayout(self.ResultLayout)
        self.MainLayout.addLayout(self.OutputLayout)
        self.LogTable = QtWidgets.QTableView(parent=self.verticalLayoutWidget_3)
        self.LogTable.setObjectName("LogTable")
        self.MainLayout.addWidget(self.LogTable)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(2, 4)

        self.retranslateUi(LogDialog)
        QtCore.QMetaObject.connectSlotsByName(LogDialog)
        LogDialog.setTabOrder(self.DataSelect, self.GetDateButton)
        LogDialog.setTabOrder(self.GetDateButton, self.StartSelect)
        LogDialog.setTabOrder(self.StartSelect, self.GetStartButton)
        LogDialog.setTabOrder(self.GetStartButton, self.EndSelect)
        LogDialog.setTabOrder(self.EndSelect, self.GetEndButton)
        LogDialog.setTabOrder(self.GetEndButton, self.ActivitiesBox)
        LogDialog.setTabOrder(self.ActivitiesBox, self.ShowActivitiesButton)
        LogDialog.setTabOrder(self.ShowActivitiesButton, self.OrderBox)
        LogDialog.setTabOrder(self.OrderBox, self.ShowOrdersButton)
        LogDialog.setTabOrder(self.ShowOrdersButton, self.NoteBox)
        LogDialog.setTabOrder(self.NoteBox, self.AddButton)
        LogDialog.setTabOrder(self.AddButton, self.UpdateButton)
        LogDialog.setTabOrder(self.UpdateButton, self.DeleteButton)
        LogDialog.setTabOrder(self.DeleteButton, self.OutputText)
        LogDialog.setTabOrder(self.OutputText, self.LogTable)

    def retranslateUi(self, LogDialog):
        _translate = QtCore.QCoreApplication.translate
        LogDialog.setWindowTitle(_translate("LogDialog", "Log"))
        self.GetDateButton.setText(_translate("LogDialog", "Get Date"))
        self.DateLabel.setText(_translate("LogDialog", "Date:"))
        self.ShowActivitiesButton.setText(_translate("LogDialog", "Show Activities"))
        self.ShowOrdersButton.setText(_translate("LogDialog", "Show Orders"))
        self.GetStartButton.setText(_translate("LogDialog", "Get Time"))
        self.StartLabel.setText(_translate("LogDialog", "Start:"))
        self.EndLabel.setText(_translate("LogDialog", "End:"))
        self.GetEndButton.setText(_translate("LogDialog", "Get Time"))
        self.ActivityLabel.setText(_translate("LogDialog", "Activity:"))
        self.OrderLabel.setText(_translate("LogDialog", "Order:"))
        self.NoteLabel.setText(_translate("LogDialog", "Note:"))
        self.AddButton.setText(_translate("LogDialog", "Add"))
        self.UpdateButton.setText(_translate("LogDialog", "Update"))
        self.DeleteButton.setText(_translate("LogDialog", "Delete"))
        self.OutputLabel.setText(_translate("LogDialog", "Result:"))
