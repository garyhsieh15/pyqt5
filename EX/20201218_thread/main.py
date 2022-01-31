import sys
import time

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget
        #QPushButton,\
        #QLineEdit, \
        #QVBoxLayout, \
        #QFormLayout, \
        #QProgressBar

from PyQt5.QtCore import QThread, \
        pyqtSignal

from UI.label import Ui_MainWindow

# 建立一個Class名為MainWindow並且繼承QMainWindow，有QMainWindow的所有功能
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # create a new thread object
        self.thread = WorkerThread()
        
        # 綁定按鈕的事件處理
        self.ui.pushButton.clicked.connect(self.execute)
        # 執行緒自定義訊號連線的槽函式
        # thread物件之singal與slot的連結
        self.thread.trigger.connect(self.display)

        # connect signal00, signal01 to slot function
        self.thread.signal00.connect(self.signal_call_00)
        self.thread.signal01.connect(self.signal_call_01)

    def execute(self):
        # 啟動執行緒,執行strar()函式則run()函式才會開始跑．
        self.thread.start()

    def display(self, _str):
        self.ui.listWidget.addItem(_str)

    def signal_call_00(self):
        print("enter signal call 00 func")

    def signal_call_01(self, val):
        print("enter signal call 01 func, val:", val)

class WorkerThread(QThread):
    # 自定義訊號物件。引數str就代表這個訊號可以傳一個字串
    trigger = pyqtSignal(str)

    signal00 = pyqtSignal()
    signal01 = pyqtSignal(int)

    #def __int__(self, parent = None):
    def __int__(self):
        # 初始化函式
        super(WorkerThread, self).__init__()
   
    def __del__(self):
        self.wait()

    # run函數結束則執行緒結束, 也就是start()結束
    def run(self):
        self.file_str = ""
        #重寫執行緒執行的run函式
        for i in range(0, 5):
            self.file_str = "File index {0}".format(i)
            # wait 1 second.
            time.sleep(1)
            # 觸發自定義訊號, 通過自定義訊號把待顯示的字串傳遞給槽函式
            self.trigger.emit(self.file_str)

            # 發射訊號執行對應的槽函數
            self.signal00.emit()
            self.signal01.emit(100)


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
