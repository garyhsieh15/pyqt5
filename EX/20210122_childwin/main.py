
from UI.mainwin import Ui_MainWindow
from UI.form import Ui_Form
from UI.form_section import Ui_Form as UiFormSection


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
        
        self.setToolTip("hint")

        #self.ui_children = UiChildren()
        #self.ui_children.setupUi(self)
        # self.child = children()生成子窗口实例self.child
        self.child = ChildrenForm()
        
        self.child_section = ChildrenFormSection()

        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.ui.actionClose.triggered.connect(self.close)
 
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.ui.actionOpen.triggered.connect(self.openMsg)

        # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
        self.ui.actionaddWin.triggered.connect(self.childShow)
        self.ui.actionsection.triggered.connect(self.child_show_section)

    def childShow(self):
        # 添加子窗口
        self.ui.gridLayout.addWidget(self.child)
        self.child.show()
       
    def child_show_section(self):
        # 添加子窗口
        self.ui.gridLayout.addWidget(self.child_section)
        self.child_section.show()


    def openMsg(self):
        #file, ok = QFileDialog.getOpenFileName(self, "打開", "/Volumes", \
        file, ok = QFileDialog.getOpenFileName(self, "打開", "/Volumes/TOSHIBA_EXT", \
                "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.ui.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

class ChildrenFormSection(QWidget, UiFormSection):
    def __init__(self):
        super(ChildrenFormSection, self).__init__()
        self.setupUi(self)



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
