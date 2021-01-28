import numpy as np
import math
import matplotlib.pyplot as plt
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

# define pi value
pi = 3.1415926

# damping ratio, ksee
#KSEE = 0.05

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

        # 設定comboBox
        self.ui.comboBox.addItem("newmark linear acc")
        self.ui.comboBox.addItem("newmark const avg acc")

        # 設定lineEdit
        self.ui.lineEdit.setText("0.05")

        # 設定progressBar
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)

    def dump_acc_data(self):
        time, up_acc, NS_acc, EW_acc = rd.read_acc_history()
        
        acc_textEdit = "time" + "\t" + "up_acc" + "\t" + "NS_acc" + "\t" + "EW_acc" + "\n"
        for i in range(0, len(time)):
            acc_textEdit += time[i] + "\t" + up_acc[i] + "\t" + NS_acc[i] + "\t" + EW_acc[i] + "\n"
        self.ui.textEdit.setPlainText(acc_textEdit)
    
    def execute(self):
        self.thread.start()

    def draw_PSA(self):
                
        if self.ui.comboBox.currentText() == "newmark linear acc":
            print("newmark linear acc method")
            
            damping_ratio = float(self.ui.lineEdit.text())

            # set natural period
            Tn = []
            Wn = []
            num = 0
            for i in np.arange(0.0, 5, 0.1):
                Tn.append(i)
                if i == 0:
                    Wn.append(10 ** 4)
                else:
                    Wn.append(2 * pi / Tn[num])
                num = num + 1

            umax = []
            PSV = []
            PSA = []
            for i in range(0, len(Tn)):
                #print("show i value: ", i)
                dis_max, pv, pa = nlacc.calc_max_respense(Wn[i], damping_ratio)
                umax.append(dis_max)
                PSV.append(pv)
                PSA.append(pa)
                
                self.ui.progressBar.setValue((i / (len(Tn) - 1)) * 100)
                # reflash windown
                QApplication.processEvents()
            # PSA - Tn
            plt.figure(figsize = (20, 6))
            plt.plot(Tn, PSA, label = "PSA - Tn, damping ratio = " + str(damping_ratio))
            plt.grid(True)
            plt.legend()
            plt.xlabel("Tn")
            plt.ylabel("PSA")

            plt.show()
            
        elif self.ui.comboBox.currentText() == "newmark const avg acc":
            print("newmark const avg acc method")
            print("self.ui.lineEdit.text(): ", self.ui.lineEdit.text())
        else:
            print("select error method !!")

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
