# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\LAYOUT_NEW2.0\register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(390, 483)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconss/header.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{background-color: rgba(250,250,250);\n"
"font:\"Arial Black\";\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 100, 331, 348))
        self.frame_2.setMinimumSize(QtCore.QSize(300, 348))
        self.frame_2.setStyleSheet("*{background-color: rgb(116, 116, 116,110);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"#pushButton{\n"
"background-color: rgb(44, 44, 44);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
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
"#lineEdit{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font-family:century gothic;\n"
"}\n"
"#lineEdit:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"#linepassword1{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font-family:century gothic;\n"
"}\n"
"#linepassword1:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"#linepassword2{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font-family:century gothic;\n"
"}\n"
"#linepassword2:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"#lineverify{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font-family:century gothic;\n"
"}\n"
"#lineverify:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"#pushButton_2{\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"}\n"
"#pushButton_2:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid  rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.linepassword1 = QtWidgets.QLineEdit(self.frame_2)
        self.linepassword1.setGeometry(QtCore.QRect(150, 180, 171, 22))
        self.linepassword1.setStyleSheet("")
        self.linepassword1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linepassword1.setClearButtonEnabled(True)
        self.linepassword1.setObjectName("linepassword1")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 141, 22))
        self.label_8.setStyleSheet("font: 13px \"Arial Black\";\n"
"background:none;")
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 91, 22))
        self.label_5.setStyleSheet("font: 11pt \"Arial Black\";\n"
"background:none;")
        self.label_5.setObjectName("label_5")
        self.linepassword2 = QtWidgets.QLineEdit(self.frame_2)
        self.linepassword2.setGeometry(QtCore.QRect(150, 210, 171, 22))
        self.linepassword2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.linepassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linepassword2.setClearButtonEnabled(True)
        self.linepassword2.setObjectName("linepassword2")
        self.lineverify = QtWidgets.QLineEdit(self.frame_2)
        self.lineverify.setGeometry(QtCore.QRect(150, 240, 171, 22))
        self.lineverify.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineverify.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineverify.setClearButtonEnabled(True)
        self.lineverify.setObjectName("lineverify")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 300, 111, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(150, 150, 171, 20))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(8)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 131, 19))
        self.label_4.setStyleSheet("font: 13px \"Arial black\";\n"
"background:none;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(60, 180, 91, 22))
        self.label_6.setStyleSheet("font: 11pt \"Arial Black\";\n"
"background:none;")
        self.label_6.setObjectName("label_6")
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(130, 20, 71, 81))
        self.toolButton.setStyleSheet("image: url(:/iconss/register_icon.png);\n"
"border-radius:40;\n"
"background:transparent;\n"
"\n"
"")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 300, 91, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(120, 110, 91, 22))
        self.label_9.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background:none;")
        self.label_9.setObjectName("label_9")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 391, 80))
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font:  14pt \"Arial Black\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setStyleSheet("font: 15pt \"Impact\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register"))
        self.linepassword1.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "Confirm Password:"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.linepassword2.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.lineverify.setPlaceholderText(_translate("MainWindow", "provided by HR officer"))
        self.pushButton.setText(_translate("MainWindow", "Back to Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Verification Code:"))
        self.label_6.setText(_translate("MainWindow", "Password: "))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.label_9.setText(_translate("MainWindow", "Register"))
        self.label_7.setText(_translate("MainWindow", "Employee Information Database"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
