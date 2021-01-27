
from UI.label import Ui_Form

import sys
import time

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButton.setCheckable(True)
        self.ui.pushButton.toggle()
        self.ui.pushButton.clicked.connect(self.btn)
        #  設定pushButton disable.
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.clicked.connect(self.close)

        # 設定radioButton_2先被選中
        self.ui.radioButton_2.setChecked(True) 

        # 設定checkBox被勾選
        self.ui.checkBox.setChecked(True)
        # 利用lamba的方式傳參數
        self.ui.checkBox.stateChanged.connect(lambda:self.checkbox(self.ui.checkBox))
        self.ui.checkBox_2.stateChanged.connect(lambda:self.checkbox(self.ui.checkBox_2))

    def btn(self):
        print("ischecked(): ", self.ui.pushButton.isChecked())
        if self.ui.pushButton.isChecked():
            print("button pressed")
        else:
            print("button released")

    def checkbox(self, btn):
        # checkBox上的文字
        print("btn.text(): ", btn.text())
        # 若被選中, isChecked()為trure.
        print("btn.isChecked(): ", btn.isChecked())
        print("btn.checkState(): ", btn.checkState())

if __name__ == '__main__':
    # 新增一個Qt應用程式，管理所有的Qt物件資源(唯一一個), 並且傳入sys.argv作為初始化資料
    # sys：用於Qt開始的參數
    # 每個Qt程式只會有一個 QApplication 作為管理所有Qt資源的管理程式
    app = QApplication(sys.argv)
    # 新增一個MainWindow物件(QMainWindow物件)
    window = MainWindow()
    # 顯示視窗
    window.show()
    # app.exec_() 進入QApplication程式，也就是說開始運行Qt GUI程式,
    # 當app.exec_()執行完畢時，關閉python。
    sys.exit(app.exec_()) 
