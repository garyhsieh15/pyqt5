# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 721, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile_F = QtWidgets.QMenu(self.menubar)
        self.menuFile_F.setObjectName("menuFile_F")
        self.menuEdit_E_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdit_E_2.setObjectName("menuEdit_E_2")
        self.menuView_V = QtWidgets.QMenu(self.menubar)
        self.menuView_V.setObjectName("menuView_V")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionaddWin = QtWidgets.QAction(MainWindow)
        self.actionaddWin.setObjectName("actionaddWin")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionsection = QtWidgets.QAction(MainWindow)
        self.actionsection.setObjectName("actionsection")
        self.menuFile_F.addAction(self.actionNew)
        self.menuFile_F.addAction(self.actionOpen)
        self.menuFile_F.addAction(self.actionClose)
        self.menuEdit_E_2.addAction(self.actionUndo)
        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuEdit_E_2.menuAction())
        self.menubar.addAction(self.menuView_V.menuAction())
        self.toolBar.addAction(self.actionaddWin)
        self.toolBar.addAction(self.actionsection)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MWin"))
        self.menuFile_F.setTitle(_translate("MainWindow", "File(&F)"))
        self.menuEdit_E_2.setTitle(_translate("MainWindow", "Edit(&E)"))
        self.menuView_V.setTitle(_translate("MainWindow", "View(&V)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionaddWin.setText(_translate("MainWindow", "addWin"))
        self.actionaddWin.setToolTip(_translate("MainWindow", "addWin"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionsection.setText(_translate("MainWindow", "section"))
        self.actionsection.setToolTip(_translate("MainWindow", "section_"))

