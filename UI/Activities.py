# Form implementation generated from reading ui file 'UI_RAW\Activities.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ActivitiesDialog(object):
    def setupUi(self, ActivitiesDialog):
        ActivitiesDialog.setObjectName("ActivitiesDialog")
        ActivitiesDialog.resize(376, 479)
        self.gridLayout = QtWidgets.QGridLayout(ActivitiesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.ActivityLayout = QtWidgets.QHBoxLayout()
        self.ActivityLayout.setObjectName("ActivityLayout")
        self.ActivityLabel = QtWidgets.QLabel(parent=ActivitiesDialog)
        self.ActivityLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.ActivityLabel.setWordWrap(False)
        self.ActivityLabel.setObjectName("ActivityLabel")
        self.ActivityLayout.addWidget(self.ActivityLabel)
        self.ActivityText = QtWidgets.QLineEdit(parent=ActivitiesDialog)
        self.ActivityText.setObjectName("ActivityText")
        self.ActivityLayout.addWidget(self.ActivityText)
        self.MainLayout.addLayout(self.ActivityLayout)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.ModificationLayout = QtWidgets.QHBoxLayout()
        self.ModificationLayout.setObjectName("ModificationLayout")
        self.AddButton = QtWidgets.QPushButton(parent=ActivitiesDialog)
        self.AddButton.setObjectName("AddButton")
        self.ModificationLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(parent=ActivitiesDialog)
        self.UpdateButton.setObjectName("UpdateButton")
        self.ModificationLayout.addWidget(self.UpdateButton)
        self.DeleteButton = QtWidgets.QPushButton(parent=ActivitiesDialog)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ModificationLayout.addWidget(self.DeleteButton)
        self.OutputLayout.addLayout(self.ModificationLayout)
        self.SearchSection = QtWidgets.QVBoxLayout()
        self.SearchSection.setObjectName("SearchSection")
        self.SearchSectionLabel = QtWidgets.QLabel(parent=ActivitiesDialog)
        self.SearchSectionLabel.setObjectName("SearchSectionLabel")
        self.SearchSection.addWidget(self.SearchSectionLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.SearchLayout = QtWidgets.QHBoxLayout()
        self.SearchLayout.setObjectName("SearchLayout")
        self.SearchLabel = QtWidgets.QLabel(parent=ActivitiesDialog)
        self.SearchLabel.setObjectName("SearchLabel")
        self.SearchLayout.addWidget(self.SearchLabel)
        self.SearchText = QtWidgets.QLineEdit(parent=ActivitiesDialog)
        self.SearchText.setObjectName("SearchText")
        self.SearchLayout.addWidget(self.SearchText)
        self.EnableSearch = QtWidgets.QCheckBox(parent=ActivitiesDialog)
        self.EnableSearch.setText("")
        self.EnableSearch.setObjectName("EnableSearch")
        self.SearchLayout.addWidget(self.EnableSearch)
        self.SearchSection.addLayout(self.SearchLayout)
        self.OutputLayout.addLayout(self.SearchSection)
        self.ResultLayout = QtWidgets.QHBoxLayout()
        self.ResultLayout.setObjectName("ResultLayout")
        self.OutputLabel = QtWidgets.QLabel(parent=ActivitiesDialog)
        self.OutputLabel.setObjectName("OutputLabel")
        self.ResultLayout.addWidget(self.OutputLabel)
        self.OutputText = QtWidgets.QLineEdit(parent=ActivitiesDialog)
        self.OutputText.setReadOnly(True)
        self.OutputText.setObjectName("OutputText")
        self.ResultLayout.addWidget(self.OutputText)
        self.OutputLayout.addLayout(self.ResultLayout)
        self.MainLayout.addLayout(self.OutputLayout)
        self.ActivityTable = QtWidgets.QTableView(parent=ActivitiesDialog)
        self.ActivityTable.setObjectName("ActivityTable")
        self.MainLayout.addWidget(self.ActivityTable)
        self.Reload = QtWidgets.QPushButton(parent=ActivitiesDialog)
        self.Reload.setObjectName("Reload")
        self.MainLayout.addWidget(self.Reload)
        self.MainLayout.setStretch(2, 3)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)

        self.retranslateUi(ActivitiesDialog)
        QtCore.QMetaObject.connectSlotsByName(ActivitiesDialog)
        ActivitiesDialog.setTabOrder(self.AddButton, self.UpdateButton)
        ActivitiesDialog.setTabOrder(self.UpdateButton, self.DeleteButton)
        ActivitiesDialog.setTabOrder(self.DeleteButton, self.OutputText)
        ActivitiesDialog.setTabOrder(self.OutputText, self.ActivityTable)

    def retranslateUi(self, ActivitiesDialog):
        _translate = QtCore.QCoreApplication.translate
        ActivitiesDialog.setWindowTitle(_translate("ActivitiesDialog", "Activities"))
        self.ActivityLabel.setText(_translate("ActivitiesDialog", "Activity:"))
        self.AddButton.setText(_translate("ActivitiesDialog", "Add"))
        self.UpdateButton.setText(_translate("ActivitiesDialog", "Update"))
        self.DeleteButton.setText(_translate("ActivitiesDialog", "Delete"))
        self.SearchSectionLabel.setText(_translate("ActivitiesDialog", "Search Options"))
        self.SearchLabel.setText(_translate("ActivitiesDialog", "Activity:"))
        self.OutputLabel.setText(_translate("ActivitiesDialog", "Result:"))
        self.Reload.setText(_translate("ActivitiesDialog", "Reload"))
