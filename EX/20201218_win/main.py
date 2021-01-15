
from UI.label import Ui_MainWindow

import sys
import time

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget, \
        QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 菜單的點擊事件，當點擊關閉菜單時連接槽函數 close()
        self.ui.actionClose.triggered.connect(self.close)
        # 菜單的點擊事件，當點擊打開菜單時連接槽函數 openMsg()
        self.ui.actionOpen.triggered.connect(self.openMsg)

    def openMsg(self):  
        file,ok= QFileDialog.getOpenFileName(self,"打開", \
                "/Volumes", \
                "All Files (*);;Text Files (*.txt)") 
	# 在狀態欄顯示文件地址  		
        self.ui.statusbar.showMessage(file)


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
