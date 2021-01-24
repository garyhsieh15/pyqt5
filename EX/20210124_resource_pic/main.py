
from UI.form import Ui_Form

import sys
import time

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget, \
        QFileDialog

from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.initUI()

        self.ui.pushButton.clicked.connect(self.close_button_click)
    
    def initUI(self):
        # 調整物件初始的大小
        self.resize(800, 450)
        # 設定初始位置與視窗的寬度, 高度
        #self.setGeometry(0, 0, 800, 450)
        # 設定初始視窗的位置
        self.move(0, 23)
        # 設定視窗的title
        self.setWindowTitle("VAI")

    #可以關掉視窗外又可以有視窗相關的參數
    def close_button_click(self):
        sender = self.sender()
        # 傳送按鈕的名稱
        print(sender.text() + ", press close")
        # 取得視窗的size
        print(self.size())
        # x dir size
        print(self.width())
        # y dir size
        print(self.height())
        # 取得視窗左上角的位置
        print(self.pos())

        qApp = QApplication.instance()
        qApp.quit()

if __name__ == '__main__':
    # 新增一個Qt應用程式，管理所有的Qt物件資源(唯一一個), 並且傳入sys.argv作為初始化資料
    # sys：用於Qt開始的參數
    # 每個Qt程式只會有一個 QApplication 作為管理所有Qt資源的管理程式
    app = QApplication(sys.argv)
    # 視窗標題添加圖示
    app.setWindowIcon(QIcon("/Volumes/TOSHIBA_EXT/data/programming/pyqt5/EX/20210124_resource_pic/cartoon2.ico"))
    # 新增一個MainWindow物件(QMainWindow物件)
    window = MainWindow()
    # 顯示視窗
    window.show()
    # app.exec_() 進入QApplication程式，也就是說開始運行Qt GUI程式,
    # 當app.exec_()執行完畢時，關閉python。
    #sys.exit(app.exec_())
    # exec_() -> old, exec() -> new method
    sys.exit(app.exec()) 
