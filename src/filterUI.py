# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\filterUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilterWindow(object):
    def setupUi(self, FilterWindow):
        FilterWindow.setObjectName("FilterWindow")
        FilterWindow.resize(592, 518)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FilterWindow.sizePolicy().hasHeightForWidth())
        FilterWindow.setSizePolicy(sizePolicy)
        FilterWindow.setMinimumSize(QtCore.QSize(500, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 217, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 187, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 78, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 105, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 206, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 217, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 187, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 78, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 105, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 206, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 78, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 217, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 187, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 78, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 105, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 78, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 78, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 157, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        FilterWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        FilterWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Pictures/Misc/car logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FilterWindow.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(FilterWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)
        self.searchBtn = QtWidgets.QPushButton(FilterWindow)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelBtn = QtWidgets.QPushButton(FilterWindow)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(FilterWindow)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 572, 450))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dateCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.dateCheck.setText("")
        self.dateCheck.setChecked(False)
        self.dateCheck.setObjectName("dateCheck")
        self.gridLayout_2.addWidget(self.dateCheck, 2, 2, 1, 1)
        self.tagLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.tagLbl.setObjectName("tagLbl")
        self.gridLayout_2.addWidget(self.tagLbl, 8, 0, 1, 1)
        self.projectLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.projectLbl.setObjectName("projectLbl")
        self.gridLayout_2.addWidget(self.projectLbl, 6, 0, 1, 1)
        self.collectorLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.collectorLbl.setObjectName("collectorLbl")
        self.gridLayout_2.addWidget(self.collectorLbl, 4, 0, 1, 1)
        self.descriptionLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.descriptionLbl.setObjectName("descriptionLbl")
        self.gridLayout_2.addWidget(self.descriptionLbl, 9, 0, 1, 1)
        self.dateLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateLbl.setObjectName("dateLbl")
        self.gridLayout_2.addWidget(self.dateLbl, 2, 0, 1, 1)
        self.carLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.carLbl.setObjectName("carLbl")
        self.gridLayout_2.addWidget(self.carLbl, 3, 0, 1, 1)
        self.subsystemLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.subsystemLbl.setObjectName("subsystemLbl")
        self.gridLayout_2.addWidget(self.subsystemLbl, 5, 0, 1, 1)
        self.nameLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLbl.setObjectName("nameLbl")
        self.gridLayout_2.addWidget(self.nameLbl, 1, 0, 1, 1)
        self.subsystemCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.subsystemCheck.setText("")
        self.subsystemCheck.setObjectName("subsystemCheck")
        self.gridLayout_2.addWidget(self.subsystemCheck, 5, 2, 1, 1)
        self.projectCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.projectCheck.setText("")
        self.projectCheck.setObjectName("projectCheck")
        self.gridLayout_2.addWidget(self.projectCheck, 6, 2, 1, 1)
        self.nameCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.nameCheck.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameCheck.setFont(font)
        self.nameCheck.setText("")
        self.nameCheck.setIconSize(QtCore.QSize(18, 18))
        self.nameCheck.setObjectName("nameCheck")
        self.gridLayout_2.addWidget(self.nameCheck, 1, 2, 1, 1)
        self.tagCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.tagCheck.setText("")
        self.tagCheck.setObjectName("tagCheck")
        self.gridLayout_2.addWidget(self.tagCheck, 8, 2, 1, 1)
        self.descCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.descCheck.setText("")
        self.descCheck.setObjectName("descCheck")
        self.gridLayout_2.addWidget(self.descCheck, 9, 2, 1, 1)
        self.enableLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enableLbl.setObjectName("enableLbl")
        self.gridLayout_2.addWidget(self.enableLbl, 0, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 9, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 1, 9, 1)
        self.carCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.carCheck.setText("")
        self.carCheck.setObjectName("carCheck")
        self.gridLayout_2.addWidget(self.carCheck, 3, 2, 1, 1)
        self.collectorCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.collectorCheck.setText("")
        self.collectorCheck.setObjectName("collectorCheck")
        self.gridLayout_2.addWidget(self.collectorCheck, 4, 2, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_2.addWidget(self.nameEdit, 1, 4, 1, 1)
        self.carDrop = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.carDrop.setEditable(False)
        self.carDrop.setObjectName("carDrop")
        self.gridLayout_2.addWidget(self.carDrop, 3, 4, 1, 1)
        self.collectorEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.collectorEdit.setObjectName("collectorEdit")
        self.gridLayout_2.addWidget(self.collectorEdit, 4, 4, 1, 1)
        self.subsystemDrop = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.subsystemDrop.setObjectName("subsystemDrop")
        self.gridLayout_2.addWidget(self.subsystemDrop, 5, 4, 1, 1)
        self.projectEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.projectEdit.setObjectName("projectEdit")
        self.gridLayout_2.addWidget(self.projectEdit, 6, 4, 1, 1)
        self.dateSelect = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateSelect.setCalendarPopup(True)
        self.dateSelect.setObjectName("dateSelect")
        self.gridLayout_2.addWidget(self.dateSelect, 2, 4, 1, 1)
        self.descriptionEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.descriptionEdit.setTabChangesFocus(True)
        self.descriptionEdit.setReadOnly(False)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout_2.addWidget(self.descriptionEdit, 9, 4, 1, 1)
        self.tagEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.tagEdit.setTabChangesFocus(True)
        self.tagEdit.setObjectName("tagEdit")
        self.gridLayout_2.addWidget(self.tagEdit, 8, 4, 1, 1)
        self.testLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.testLbl.setObjectName("testLbl")
        self.gridLayout_2.addWidget(self.testLbl, 7, 0, 1, 1)
        self.testCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.testCheck.setText("")
        self.testCheck.setObjectName("testCheck")
        self.gridLayout_2.addWidget(self.testCheck, 7, 2, 1, 1)
        self.testEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.testEdit.setObjectName("testEdit")
        self.gridLayout_2.addWidget(self.testEdit, 7, 4, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 2, 1)
        self.tagLbl.setBuddy(self.tagEdit)
        self.projectLbl.setBuddy(self.projectEdit)
        self.collectorLbl.setBuddy(self.collectorEdit)
        self.descriptionLbl.setBuddy(self.descriptionEdit)
        self.dateLbl.setBuddy(self.dateSelect)
        self.carLbl.setBuddy(self.carDrop)
        self.subsystemLbl.setBuddy(self.subsystemDrop)
        self.nameLbl.setBuddy(self.nameEdit)

        self.retranslateUi(FilterWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterWindow)
        FilterWindow.setTabOrder(self.nameEdit, self.dateSelect)
        FilterWindow.setTabOrder(self.dateSelect, self.carDrop)
        FilterWindow.setTabOrder(self.carDrop, self.collectorEdit)
        FilterWindow.setTabOrder(self.collectorEdit, self.subsystemDrop)
        FilterWindow.setTabOrder(self.subsystemDrop, self.projectEdit)
        FilterWindow.setTabOrder(self.projectEdit, self.tagEdit)
        FilterWindow.setTabOrder(self.tagEdit, self.descriptionEdit)
        FilterWindow.setTabOrder(self.descriptionEdit, self.searchBtn)
        FilterWindow.setTabOrder(self.searchBtn, self.cancelBtn)
        FilterWindow.setTabOrder(self.cancelBtn, self.scrollArea)

    def retranslateUi(self, FilterWindow):
        _translate = QtCore.QCoreApplication.translate
        FilterWindow.setWindowTitle(_translate("FilterWindow", "RIT Baja Database"))
        self.searchBtn.setText(_translate("FilterWindow", "Search Data"))
        self.cancelBtn.setText(_translate("FilterWindow", "Cancel"))
        self.tagLbl.setToolTip(_translate("FilterWindow", "Tags for data, separate with commas"))
        self.tagLbl.setText(_translate("FilterWindow", "Tags"))
        self.projectLbl.setToolTip(_translate("FilterWindow", "What project is this for?"))
        self.projectLbl.setText(_translate("FilterWindow", "Project Name"))
        self.collectorLbl.setToolTip(_translate("FilterWindow", "Who Collected the data?"))
        self.collectorLbl.setText(_translate("FilterWindow", "Collector"))
        self.descriptionLbl.setToolTip(_translate("FilterWindow", "What is this data?"))
        self.descriptionLbl.setText(_translate("FilterWindow", "Description"))
        self.dateLbl.setToolTip(_translate("FilterWindow", "When was this data collected?"))
        self.dateLbl.setText(_translate("FilterWindow", "Date Collected"))
        self.carLbl.setToolTip(_translate("FilterWindow", "What car was this data collected with/for?"))
        self.carLbl.setText(_translate("FilterWindow", "Car Name"))
        self.subsystemLbl.setToolTip(_translate("FilterWindow", "What team subgroup is this for?"))
        self.subsystemLbl.setText(_translate("FilterWindow", "Subsystem"))
        self.nameLbl.setToolTip(_translate("FilterWindow", "Name for the data"))
        self.nameLbl.setText(_translate("FilterWindow", "Name"))
        self.enableLbl.setText(_translate("FilterWindow", "Filter by:"))
        self.dateSelect.setDisplayFormat(_translate("FilterWindow", "MM/dd/yyyy"))
        self.tagEdit.setPlaceholderText(_translate("FilterWindow", "Tags, separated with commas"))
        self.testLbl.setText(_translate("FilterWindow", "Test Plan"))


