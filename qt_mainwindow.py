# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainWindow.ui'
#
# Created: Tue Dec 17 18:55:38 2013
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(360, 370))
        MainWindow.setMaximumSize(QtCore.QSize(360, 370))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 341, 151))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 57, 14))
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(210, 10, 140, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.energy = QtWidgets.QSpinBox(self.widget)
        self.energy.setMaximum(9999999)
        self.energy.setSingleStep(100)
        self.energy.setProperty("value", 100)
        self.energy.setObjectName("energy")
        self.gridLayout.addWidget(self.energy, 1, 1, 1, 1)
        self.pixels_label = QtWidgets.QLabel(self.widget)
        self.pixels_label.setObjectName("pixels_label")
        self.gridLayout.addWidget(self.pixels_label, 2, 0, 1, 1)
        self.pixels = QtWidgets.QSpinBox(self.widget)
        self.pixels.setMaximum(9999999)
        self.pixels.setSingleStep(100)
        self.pixels.setObjectName("pixels")
        self.gridLayout.addWidget(self.pixels, 2, 1, 1, 1)
        self.health_label = QtWidgets.QLabel(self.widget)
        self.health_label.setObjectName("health_label")
        self.gridLayout.addWidget(self.health_label, 0, 0, 1, 1)
        self.health = QtWidgets.QSpinBox(self.widget)
        self.health.setMaximum(9999999)
        self.health.setSingleStep(100)
        self.health.setProperty("value", 100)
        self.health.setObjectName("health")
        self.gridLayout.addWidget(self.health, 0, 1, 1, 1)
        self.energy_label = QtWidgets.QLabel(self.widget)
        self.energy_label.setObjectName("energy_label")
        self.gridLayout.addWidget(self.energy_label, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.name_label = QtWidgets.QLabel(self.widget1)
        self.name_label.setObjectName("name_label")
        self.gridLayout_2.addWidget(self.name_label, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.widget1)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.race_label = QtWidgets.QLabel(self.widget1)
        self.race_label.setObjectName("race_label")
        self.gridLayout_2.addWidget(self.race_label, 1, 0, 1, 1)
        self.race = QtWidgets.QComboBox(self.widget1)
        self.race.setObjectName("race")
        self.gridLayout_2.addWidget(self.race, 1, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(30, 80, 151, 41))
        self.widget2.setObjectName("widget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gender_label = QtWidgets.QLabel(self.widget2)
        self.gender_label.setObjectName("gender_label")
        self.gridLayout_3.addWidget(self.gender_label, 0, 0, 1, 1)
        self.widget3 = QtWidgets.QWidget(self.widget2)
        self.widget3.setObjectName("widget3")
        self.male = QtWidgets.QRadioButton(self.widget3)
        self.male.setGeometry(QtCore.QRect(0, 0, 57, 19))
        self.male.setObjectName("male")
        self.female = QtWidgets.QRadioButton(self.widget3)
        self.female.setGeometry(QtCore.QRect(0, 20, 72, 19))
        self.female.setObjectName("female")
        self.gridLayout_3.addWidget(self.widget3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Main Bag"))
        self.pixels_label.setText(_translate("MainWindow", "Pixels"))
        self.health_label.setText(_translate("MainWindow", "Health"))
        self.energy_label.setText(_translate("MainWindow", "Energy"))
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.race_label.setText(_translate("MainWindow", "Race"))
        self.gender_label.setText(_translate("MainWindow", "Gender"))
        self.male.setText(_translate("MainWindow", "Male"))
        self.female.setText(_translate("MainWindow", "Female"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a player save file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save player changes"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit program"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
