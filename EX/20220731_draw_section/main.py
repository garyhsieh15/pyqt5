# -*- coding: utf-8 -*-
 

from UI.label import Ui_MainWindow

import sys
import time

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget, \
        QFileDialog, \
        QVBoxLayout, \
        QLabel

from PyQt5.QtCore import QDir, \
        Qt
from PyQt5.QtGui import QPixmap, \
        QPainter, \
        QBrush

#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *


class Drawing(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self):
        self.setGeometry(300, 300, 865, 280)

        lab1 = QLabel()
        lab1.setPixmap(QPixmap("../images/python.jpg"))
        vbox=QVBoxLayout()
        vbox.addWidget(lab1)

        self.setLayout(vbox)
        self.setWindowTitle('win pic')
        self.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setGeometry(1200, 600, 730, 280)
        self.setWindowTitle("gary")
        #self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        #qp.drawRect(10, 15, 90, 60)
        #           x,   y,  delta x, delta y
        qp.drawRect(0, 0, 40, 30)

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)

if __name__ == '__main__':
    # 新增一個Qt應用程式，管理所有的Qt物件資源(唯一一個), 並且傳入sys.argv作為初始化資料
    # sys：用於Qt開始的參數
    # 每個Qt程式只會有一個 QApplication 作為管理所有Qt資源的管理程式
    app = QApplication(sys.argv)
    # 新增一個MainWindow物件(QMainWindow物件)
    window = MainWindow()
    demo = Drawing()

    # 顯示視窗
    window.show()
    demo.show()
    # app.exec_() 進入QApplication程式，也就是說開始運行Qt GUI程式,
    # 當app.exec_()執行完畢時，關閉python。
    sys.exit(app.exec_()) 

