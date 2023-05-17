# Form implementation generated from reading ui file 'UI_RAW\Customers.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CustomerDialog(object):
    def setupUi(self, CustomerDialog):
        CustomerDialog.setObjectName("CustomerDialog")
        CustomerDialog.resize(1132, 911)
        self.gridLayout = QtWidgets.QGridLayout(CustomerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.SelectionGrid = QtWidgets.QGridLayout()
        self.SelectionGrid.setObjectName("SelectionGrid")
        self.PhoneText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.PhoneText.setObjectName("PhoneText")
        self.SelectionGrid.addWidget(self.PhoneText, 3, 2, 1, 1)
        self.StatusLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.StatusLabel.setObjectName("StatusLabel")
        self.SelectionGrid.addWidget(self.StatusLabel, 6, 0, 1, 1)
        self.SocialText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.SocialText.setObjectName("SocialText")
        self.SelectionGrid.addWidget(self.SocialText, 4, 2, 1, 1)
        self.CompanyText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.CompanyText.setObjectName("CompanyText")
        self.SelectionGrid.addWidget(self.CompanyText, 0, 2, 1, 1)
        self.EmailLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.EmailLabel.setObjectName("EmailLabel")
        self.SelectionGrid.addWidget(self.EmailLabel, 2, 0, 1, 1)
        self.CustomerNote = QtWidgets.QLabel(parent=CustomerDialog)
        self.CustomerNote.setObjectName("CustomerNote")
        self.SelectionGrid.addWidget(self.CustomerNote, 7, 0, 1, 1)
        self.AddressLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.AddressLabel.setObjectName("AddressLabel")
        self.SelectionGrid.addWidget(self.AddressLabel, 5, 0, 1, 1)
        self.PhoneLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.SelectionGrid.addWidget(self.PhoneLabel, 3, 0, 1, 1)
        self.NoteText = QtWidgets.QTextEdit(parent=CustomerDialog)
        self.NoteText.setObjectName("NoteText")
        self.SelectionGrid.addWidget(self.NoteText, 7, 2, 1, 1)
        self.StatusBox = QtWidgets.QComboBox(parent=CustomerDialog)
        self.StatusBox.setObjectName("StatusBox")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.StatusBox.addItem("")
        self.SelectionGrid.addWidget(self.StatusBox, 6, 2, 1, 1)
        self.SocialLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.SocialLabel.setObjectName("SocialLabel")
        self.SelectionGrid.addWidget(self.SocialLabel, 4, 0, 1, 1)
        self.ContactText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.ContactText.setObjectName("ContactText")
        self.SelectionGrid.addWidget(self.ContactText, 1, 2, 1, 1)
        self.AddressText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.AddressText.setObjectName("AddressText")
        self.SelectionGrid.addWidget(self.AddressText, 5, 2, 1, 1)
        self.EmailText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.EmailText.setObjectName("EmailText")
        self.SelectionGrid.addWidget(self.EmailText, 2, 2, 1, 1)
        self.CompanyLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.CompanyLabel.setObjectName("CompanyLabel")
        self.SelectionGrid.addWidget(self.CompanyLabel, 0, 0, 1, 1)
        self.ContactLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.ContactLabel.setObjectName("ContactLabel")
        self.SelectionGrid.addWidget(self.ContactLabel, 1, 0, 1, 1)
        self.InputLayout.addLayout(self.SelectionGrid)
        self.MainLayout.addLayout(self.InputLayout)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.ModificationLayout = QtWidgets.QHBoxLayout()
        self.ModificationLayout.setObjectName("ModificationLayout")
        self.AddButton = QtWidgets.QPushButton(parent=CustomerDialog)
        self.AddButton.setObjectName("AddButton")
        self.ModificationLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(parent=CustomerDialog)
        self.UpdateButton.setObjectName("UpdateButton")
        self.ModificationLayout.addWidget(self.UpdateButton)
        self.DeleteButton = QtWidgets.QPushButton(parent=CustomerDialog)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ModificationLayout.addWidget(self.DeleteButton)
        self.OutputLayout.addLayout(self.ModificationLayout)
        self.SearchLayout = QtWidgets.QVBoxLayout()
        self.SearchLayout.setObjectName("SearchLayout")
        self.SearchLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.SearchLabel.setObjectName("SearchLabel")
        self.SearchLayout.addWidget(self.SearchLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.SearchSplit = QtWidgets.QHBoxLayout()
        self.SearchSplit.setObjectName("SearchSplit")
        self.SearchLeft = QtWidgets.QGridLayout()
        self.SearchLeft.setObjectName("SearchLeft")
        self.EmailSearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.EmailSearchL.setObjectName("EmailSearchL")
        self.SearchLeft.addWidget(self.EmailSearchL, 1, 0, 1, 1)
        self.CompanyEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.CompanyEnable.setText("")
        self.CompanyEnable.setObjectName("CompanyEnable")
        self.SearchLeft.addWidget(self.CompanyEnable, 0, 2, 1, 1)
        self.CompanySearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.CompanySearchL.setObjectName("CompanySearchL")
        self.SearchLeft.addWidget(self.CompanySearchL, 0, 0, 1, 1)
        self.CompanySearch = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.CompanySearch.setObjectName("CompanySearch")
        self.SearchLeft.addWidget(self.CompanySearch, 0, 1, 1, 1)
        self.SocialSearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.SocialSearchL.setObjectName("SocialSearchL")
        self.SearchLeft.addWidget(self.SocialSearchL, 2, 0, 1, 1)
        self.EmailSearch = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.EmailSearch.setObjectName("EmailSearch")
        self.SearchLeft.addWidget(self.EmailSearch, 1, 1, 1, 1)
        self.SocialSearch = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.SocialSearch.setObjectName("SocialSearch")
        self.SearchLeft.addWidget(self.SocialSearch, 2, 1, 1, 1)
        self.EmailEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.EmailEnable.setText("")
        self.EmailEnable.setObjectName("EmailEnable")
        self.SearchLeft.addWidget(self.EmailEnable, 1, 2, 1, 1)
        self.SocialEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.SocialEnable.setText("")
        self.SocialEnable.setObjectName("SocialEnable")
        self.SearchLeft.addWidget(self.SocialEnable, 2, 2, 1, 1)
        self.SearchSplit.addLayout(self.SearchLeft)
        self.SearchRight = QtWidgets.QGridLayout()
        self.SearchRight.setObjectName("SearchRight")
        self.AddressSearch = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.AddressSearch.setObjectName("AddressSearch")
        self.SearchRight.addWidget(self.AddressSearch, 2, 1, 1, 1)
        self.PhoneEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.PhoneEnable.setText("")
        self.PhoneEnable.setObjectName("PhoneEnable")
        self.SearchRight.addWidget(self.PhoneEnable, 1, 2, 1, 1)
        self.ContactSearch = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.ContactSearch.setObjectName("ContactSearch")
        self.SearchRight.addWidget(self.ContactSearch, 0, 1, 1, 1)
        self.PhoneSearch = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.PhoneSearch.setObjectName("PhoneSearch")
        self.SearchRight.addWidget(self.PhoneSearch, 1, 1, 1, 1)
        self.ContactEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.ContactEnable.setText("")
        self.ContactEnable.setObjectName("ContactEnable")
        self.SearchRight.addWidget(self.ContactEnable, 0, 2, 1, 1)
        self.PhoneSearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.PhoneSearchL.setObjectName("PhoneSearchL")
        self.SearchRight.addWidget(self.PhoneSearchL, 1, 0, 1, 1)
        self.AddressSearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.AddressSearchL.setObjectName("AddressSearchL")
        self.SearchRight.addWidget(self.AddressSearchL, 2, 0, 1, 1)
        self.AddressEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.AddressEnable.setText("")
        self.AddressEnable.setObjectName("AddressEnable")
        self.SearchRight.addWidget(self.AddressEnable, 2, 2, 1, 1)
        self.ContactSearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.ContactSearchL.setObjectName("ContactSearchL")
        self.SearchRight.addWidget(self.ContactSearchL, 0, 0, 1, 1)
        self.SearchSplit.addLayout(self.SearchRight)
        self.SearchLayout.addLayout(self.SearchSplit)
        self.StatusSearchSec = QtWidgets.QHBoxLayout()
        self.StatusSearchSec.setObjectName("StatusSearchSec")
        self.StatusSearchL = QtWidgets.QLabel(parent=CustomerDialog)
        self.StatusSearchL.setObjectName("StatusSearchL")
        self.StatusSearchSec.addWidget(self.StatusSearchL)
        self.StatusComboSearch = QtWidgets.QComboBox(parent=CustomerDialog)
        self.StatusComboSearch.setObjectName("StatusComboSearch")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.StatusComboSearch.addItem("")
        self.StatusSearchSec.addWidget(self.StatusComboSearch)
        self.StatusEnable = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.StatusEnable.setText("")
        self.StatusEnable.setObjectName("StatusEnable")
        self.StatusSearchSec.addWidget(self.StatusEnable)
        self.StatusSearchSec.setStretch(1, 1)
        self.SearchLayout.addLayout(self.StatusSearchSec)
        self.DateLayout = QtWidgets.QGridLayout()
        self.DateLayout.setObjectName("DateLayout")
        self.DateSelection = QtWidgets.QComboBox(parent=CustomerDialog)
        self.DateSelection.setObjectName("DateSelection")
        self.DateSelection.addItem("")
        self.DateSelection.addItem("")
        self.DateLayout.addWidget(self.DateSelection, 0, 1, 1, 1)
        self.EnableDate = QtWidgets.QCheckBox(parent=CustomerDialog)
        self.EnableDate.setText("")
        self.EnableDate.setObjectName("EnableDate")
        self.DateLayout.addWidget(self.EnableDate, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.StartDateLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.StartDateLabel.setObjectName("StartDateLabel")
        self.DateLayout.addWidget(self.StartDateLabel, 1, 0, 1, 1)
        self.DateLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.DateLabel.setObjectName("DateLabel")
        self.DateLayout.addWidget(self.DateLabel, 0, 0, 1, 1)
        self.EndDateLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.EndDateLabel.setObjectName("EndDateLabel")
        self.DateLayout.addWidget(self.EndDateLabel, 2, 0, 1, 1)
        self.StartDate = QtWidgets.QDateEdit(parent=CustomerDialog)
        self.StartDate.setObjectName("StartDate")
        self.DateLayout.addWidget(self.StartDate, 1, 1, 1, 1)
        self.EndDate = QtWidgets.QDateEdit(parent=CustomerDialog)
        self.EndDate.setObjectName("EndDate")
        self.DateLayout.addWidget(self.EndDate, 2, 1, 1, 1)
        self.GetStartDate = QtWidgets.QPushButton(parent=CustomerDialog)
        self.GetStartDate.setObjectName("GetStartDate")
        self.DateLayout.addWidget(self.GetStartDate, 1, 2, 1, 1)
        self.GetEndDate = QtWidgets.QPushButton(parent=CustomerDialog)
        self.GetEndDate.setObjectName("GetEndDate")
        self.DateLayout.addWidget(self.GetEndDate, 2, 2, 1, 1)
        self.DateLayout.setColumnStretch(1, 1)
        self.SearchLayout.addLayout(self.DateLayout)
        self.OutputLayout.addLayout(self.SearchLayout)
        self.ResultLayout = QtWidgets.QHBoxLayout()
        self.ResultLayout.setObjectName("ResultLayout")
        self.OutputLabel = QtWidgets.QLabel(parent=CustomerDialog)
        self.OutputLabel.setObjectName("OutputLabel")
        self.ResultLayout.addWidget(self.OutputLabel)
        self.OutputText = QtWidgets.QLineEdit(parent=CustomerDialog)
        self.OutputText.setReadOnly(True)
        self.OutputText.setObjectName("OutputText")
        self.ResultLayout.addWidget(self.OutputText)
        self.OutputLayout.addLayout(self.ResultLayout)
        self.MainLayout.addLayout(self.OutputLayout)
        self.CustomerTable = QtWidgets.QTableView(parent=CustomerDialog)
        self.CustomerTable.setObjectName("CustomerTable")
        self.MainLayout.addWidget(self.CustomerTable)
        self.Reload = QtWidgets.QPushButton(parent=CustomerDialog)
        self.Reload.setObjectName("Reload")
        self.MainLayout.addWidget(self.Reload)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(2, 4)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)

        self.retranslateUi(CustomerDialog)
        QtCore.QMetaObject.connectSlotsByName(CustomerDialog)
        CustomerDialog.setTabOrder(self.CompanyText, self.ContactText)
        CustomerDialog.setTabOrder(self.ContactText, self.EmailText)
        CustomerDialog.setTabOrder(self.EmailText, self.PhoneText)
        CustomerDialog.setTabOrder(self.PhoneText, self.AddressText)
        CustomerDialog.setTabOrder(self.AddressText, self.StatusBox)
        CustomerDialog.setTabOrder(self.StatusBox, self.NoteText)
        CustomerDialog.setTabOrder(self.NoteText, self.AddButton)
        CustomerDialog.setTabOrder(self.AddButton, self.UpdateButton)
        CustomerDialog.setTabOrder(self.UpdateButton, self.DeleteButton)
        CustomerDialog.setTabOrder(self.DeleteButton, self.OutputText)
        CustomerDialog.setTabOrder(self.OutputText, self.CustomerTable)

    def retranslateUi(self, CustomerDialog):
        _translate = QtCore.QCoreApplication.translate
        CustomerDialog.setWindowTitle(_translate("CustomerDialog", "Customers"))
        self.StatusLabel.setText(_translate("CustomerDialog", "Status:"))
        self.EmailLabel.setText(_translate("CustomerDialog", "Email:"))
        self.CustomerNote.setText(_translate("CustomerDialog", "Note:"))
        self.AddressLabel.setText(_translate("CustomerDialog", "Address:"))
        self.PhoneLabel.setText(_translate("CustomerDialog", "Phone Number:"))
        self.StatusBox.setItemText(0, _translate("CustomerDialog", "Good Standing"))
        self.StatusBox.setItemText(1, _translate("CustomerDialog", "On The Fence"))
        self.StatusBox.setItemText(2, _translate("CustomerDialog", "Blacklisted"))
        self.SocialLabel.setText(_translate("CustomerDialog", "Social Media:"))
        self.CompanyLabel.setText(_translate("CustomerDialog", "Company Name:"))
        self.ContactLabel.setText(_translate("CustomerDialog", "Contact Name:"))
        self.AddButton.setText(_translate("CustomerDialog", "Add"))
        self.UpdateButton.setText(_translate("CustomerDialog", "Update"))
        self.DeleteButton.setText(_translate("CustomerDialog", "Delete"))
        self.SearchLabel.setText(_translate("CustomerDialog", "Search Options"))
        self.EmailSearchL.setText(_translate("CustomerDialog", "Email:"))
        self.CompanySearchL.setText(_translate("CustomerDialog", "Company:"))
        self.SocialSearchL.setText(_translate("CustomerDialog", "Social:"))
        self.PhoneSearchL.setText(_translate("CustomerDialog", "Phone:"))
        self.AddressSearchL.setText(_translate("CustomerDialog", "Address:"))
        self.ContactSearchL.setText(_translate("CustomerDialog", "Contact:"))
        self.StatusSearchL.setText(_translate("CustomerDialog", "Status:"))
        self.StatusComboSearch.setItemText(0, _translate("CustomerDialog", "Good Standing"))
        self.StatusComboSearch.setItemText(1, _translate("CustomerDialog", "On The Fence"))
        self.StatusComboSearch.setItemText(2, _translate("CustomerDialog", "Blacklisted"))
        self.DateSelection.setItemText(0, _translate("CustomerDialog", "Last Order"))
        self.DateSelection.setItemText(1, _translate("CustomerDialog", "Last Finished Order"))
        self.StartDateLabel.setText(_translate("CustomerDialog", "Start Date:"))
        self.DateLabel.setText(_translate("CustomerDialog", "Date Type:"))
        self.EndDateLabel.setText(_translate("CustomerDialog", "End Date:"))
        self.GetStartDate.setText(_translate("CustomerDialog", "Get Date"))
        self.GetEndDate.setText(_translate("CustomerDialog", "Get Date"))
        self.OutputLabel.setText(_translate("CustomerDialog", "Result:"))
        self.Reload.setText(_translate("CustomerDialog", "Reload"))
