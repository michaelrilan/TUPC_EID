from LEAVE import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class newWindow(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(newWindow, self).__init__()
        self.setupUi(self)
        self.label_28.hide()
        self.nextPeriod_2.hide()
        self.frame_2.hide()
        self.nextPeriod.clicked.connect(self.wa1)
        self.nextPeriod_2.clicked.connect(self.wa2)
        self.nextLeave.clicked.connect(self.wa3)
        self.nextLeave_2.clicked.connect(self.wa4)



    def wa1(self):
        self.nextPeriod_2.show()
        self.nextPeriod.hide()
        x1 = int(self.lineEdit_109.text())
        xx1 = x1 + 1
        self.lineEdit_109.setText(str(xx1))
    def wa2(self):
        self.nextPeriod_2.hide()
        self.nextPeriod.show()
        x2 = int(self.lineEdit_109.text())
        xx2 = x2 - 1
        self.lineEdit_109.setText(str(xx2))
    def wa3(self):
        self.nextLeave.hide()
        self.nextLeave_2.show()
        self.label_28.show()
        self.label_29.hide()
        self.frame_2.show()
    def wa4(self):
        self.nextLeave.show()
        self.nextLeave_2.hide()
        self.label_29.show()
        self.label_28.hide()
        self.frame_2.hide()






if __name__ == "__main__":
    apps = QtWidgets.QApplication(sys.argv)
    w1 = newWindow()
    w1.show()
    apps.exec_()