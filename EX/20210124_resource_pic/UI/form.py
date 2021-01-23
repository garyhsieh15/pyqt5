# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(779, 478)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 10, 471, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("python.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(480, 310, 111, 91))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cartoon3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 331, 221, 121))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("python.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Yes"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

