# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\LAYOUT_NEW2.0\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 418)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconss/header.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(250,250,250);\n"
"font: 87 8pt \"Arial Black\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 381, 71))
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font:  14pt \"Arial\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(60, 100, 261, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("*{background-color: rgb(116, 116, 116,110);\n"
"border-radius:12px;\n"
"\n"
"}\n"
"#label_2{\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"}\n"
"#label_4{\n"
"background:transparent;\n"
"font-size: 13pt;\n"
"}\n"
"#label_3{\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"}\n"
"#pushButton{\n"
"background-color: rgb(44, 44, 44);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";\n"
"border-radius:15px;\n"
"display: inline-block;\n"
"padding: 0.5em 1em;\n"
"text-decoration: none;\n"
"border-bottom:3px solid  rgb(0,0,0);\n"
"border-right:3px solid  rgb(0,0,0);\n"
"}\n"
"#pushButton:hover{\n"
"background-color: rgb(0, 0, 0,230);\n"
"\n"
"\n"
"}\n"
"\n"
"#pushButton2{\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";\n"
"border-radius:15px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"}\n"
"#pushButton2:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid  rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#lineusername{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font:Arial;\n"
"}\n"
"#lineusername:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"#linepassword{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"}\n"
"#linepassword:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"label_4{\n"
"background:transparent;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineusername = QtWidgets.QLineEdit(self.frame_2)
        self.lineusername.setGeometry(QtCore.QRect(110, 130, 131, 20))
        self.lineusername.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineusername.setClearButtonEnabled(True)
        self.lineusername.setObjectName("lineusername")
        self.linepassword = QtWidgets.QLineEdit(self.frame_2)
        self.linepassword.setGeometry(QtCore.QRect(110, 170, 131, 20))
        self.linepassword.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.linepassword.setFrame(True)
        self.linepassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linepassword.setClearButtonEnabled(True)
        self.linepassword.setObjectName("linepassword")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 81, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(90, 20, 81, 51))
        self.toolButton.setStyleSheet("image: url(:/iconss/login_icon.png);\n"
"background:transparent;")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(100, 80, 61, 21))
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setObjectName("label_4")
        self.pushButton2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton2.setGeometry(QtCore.QRect(130, 220, 91, 31))
        self.pushButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton2.setStyleSheet("")
        self.pushButton2.setObjectName("pushButton2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Loginform"))
        self.label_7.setText(_translate("MainWindow", "Employee Information Database"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.lineusername.setPlaceholderText(_translate("MainWindow", "Username"))
        self.linepassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton2.setText(_translate("MainWindow", "Register"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
