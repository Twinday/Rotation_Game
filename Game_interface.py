# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(700, 50, 75, 23))
        self.StartButton.setObjectName("StartButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 631))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)
        self.labelLevel = QtWidgets.QLabel(self.centralwidget)
        self.labelLevel.setGeometry(QtCore.QRect(690, 150, 141, 61))
        self.labelLevel.setText("")
        self.labelLevel.setObjectName("labelLevel")
        self.labelScore = QtWidgets.QLabel(self.centralwidget)
        self.labelScore.setGeometry(QtCore.QRect(690, 300, 141, 71))
        self.labelScore.setText("")
        self.labelScore.setObjectName("labelScore")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        self.label_timer.setGeometry(QtCore.QRect(680, 470, 141, 81))
        self.label_timer.setText("")
        self.label_timer.setObjectName("label_timer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Start"))

