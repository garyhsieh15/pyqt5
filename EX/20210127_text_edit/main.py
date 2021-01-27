
import sys
import time
import read_data as rd
import newmark as nlacc

from PyQt5.QtWidgets import QApplication, \
        QMainWindow, \
        QWidget, \
        QFileDialog

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, \
        pyqtSignal
from UI.label import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # set form title name
        self.setWindowTitle("Spectrum diagram")

        self.thread = WorkerThread()

        self.ui.pushButton.clicked.connect(self.dump_acc_data)
        self.ui.pushButton_2.clicked.connect(self.execute)
        self.ui.pushButton_3.clicked.connect(self.close)

        self.thread.trigger.connect(self.draw_PSA)

    def dump_acc_data(self):
        time, up_acc, NS_acc, EW_acc = rd.read_acc_history()
        
        acc_textEdit = "time" + "\t" + "up_acc" + "\t" + "NS_acc" + "\t" + "EW_acc" + "\n"
        for i in range(0, len(time)):
            acc_textEdit += time[i] + "\t" + up_acc[i] + "\t" + NS_acc[i] + "\t" + EW_acc[i] + "\n"
        self.ui.textEdit.setPlainText(acc_textEdit)
    
    def execute(self):
        self.thread.start()

    def draw_PSA(self):
        nlacc.newmark_linear_acc()

class WorkerThread(QThread):
    # 自定義訊號物件。引數str就代表這個訊號可以傳一個字串
    trigger = pyqtSignal()
    
    #def __int__(self, parent = None):
    def __int__(self):
        # 初始化函式
        super(WorkerThread, self).__init__()
   
    def __del__(self):
        self.wait()

    # run函數結束則執行緒結束, 也就是start()結束
    def run(self):
        #重寫執行緒執行的run函式
        #觸發自定義訊號
        # time.sleep(1)
        # time.sleep(0.5)
        # 通過自定義訊號把待顯示的字串傳遞給槽函式
        self.trigger.emit()


if __name__ == '__main__':
    # 新增一個Qt應用程式，管理所有的Qt物件資源(唯一一個), 並且傳入sys.argv作為初始化資料
    # sys：用於Qt開始的參數
    # 每個Qt程式只會有一個 QApplication 作為管理所有Qt資源的管理程式
    app = QApplication(sys.argv)
    # 視窗標題添加圖示
    app.setWindowIcon(QIcon("/Volumes/TOSHIBA_EXT/data/programming/pyqt5/EX/20210127_text_edit/acc.png"))
    # 新增一個MainWindow物件(QMainWindow物件)
    window = MainWindow()
    # 顯示視窗
    window.show()
    # app.exec_() 進入QApplication程式，也就是說開始運行Qt GUI程式,
    # 當app.exec_()執行完畢時，關閉python。
    #sys.exit(app.exec_())
    # exec_() -> old, exec() -> new method
    sys.exit(app.exec()) 
