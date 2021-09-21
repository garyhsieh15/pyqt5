import numpy as np
import math
import matplotlib.pyplot as plt
import sys
import time

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget, \
        QFileDialog, \
        QMessageBox

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, \
        pyqtSignal
from UI_package.label import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # >>> create Ui_From object
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # set form title name
        self.setWindowTitle("message box")

        self.ui.pushButton.clicked.connect(self.msg)
        self.ui.pushButton_2.clicked.connect(self.close)

        # >>> create QMessageBox object
        self.msgBox = QMessageBox()

    def msg(self):
        # show chr '!' icon
        self.msgBox.setIcon(QMessageBox.Information)
        # show message content.
        self.msgBox.setText("show context!!")
        # show yes and no button.
        #self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # show OK and Cancel button.
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        reValue = self.msgBox.exec()
        if reValue == self.msgBox.Ok:
            print(">>> Ok clicked")
        elif reValue == self.msgBox.Cancel:
            print(">>> Cancel clicked")
        else:
            print(">>> occure error!!")

if __name__ == '__main__':
    # 新增一個Qt應用程式，管理所有的Qt物件資源(唯一一個), 並且傳入sys.argv作為初始化資料
    # sys：用於Qt開始的參數
    # 每個Qt程式只會有一個 QApplication 作為管理所有Qt資源的管理程式
    app = QApplication(sys.argv)
    # 視窗標題添加圖示
    #app.setWindowIcon(QIcon("/Volumes/TOSHIBA_EXT/data/programming/pyqt5/EX/path"))
    # 新增一個MainWindow物件(QMainWindow物件)
    window = MainWindow()
    # 顯示視窗
    window.show()
    # app.exec_() 進入QApplication程式，也就是說開始運行Qt GUI程式,
    # 當app.exec_()執行完畢時，關閉python。
    #sys.exit(app.exec_())
    # exec_() -> old, exec() -> new method
    sys.exit(app.exec()) 
