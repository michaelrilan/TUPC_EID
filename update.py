# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\EID_final\update.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowupd(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 566)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconss/header.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("*{\n"
"color:black;\n"
"\n"
"}\n"
"#frameAdd_2{\n"
"background-color:rgb(250,250,250)\n"
"}\n"
"#frame_4{\n"
"\n"
"background-color: rgb(0, 0, 0,32);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QLabel{\n"
"background:transparent;\n"
"}\n"
"#frame_8{\n"
"background:transparent;\n"
"border:1px solid black;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"#groupBox_7{\n"
"background:transparent;\n"
"border:1px solid black;\n"
"border-radius:8px\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font-size:9pt;\n"
"font-family:century gothic;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"#comboBox_3{\n"
"font-family:century gothic;\n"
"}\n"
"#pushmenuin1{\n"
"background-color: rgb(255, 255, 255,40);\n"
"}\n"
"\n"
"#pushmenuin1:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#pushAdd{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:5px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"color:white;\n"
"}\n"
"#pushAdd:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#pushbrowsepic{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:5px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"color:white;\n"
"}\n"
"#pushbrowsepic:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#pushtakephoto{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:5px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"color:white;\n"
"}\n"
"#pushtakephoto:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#textEdit{\n"
"border:1px solid black;\n"
"border-radius:8px;\n"
"font-size:9pt;\n"
"font-family:century gothic;\n"
"\n"
"}\n"
"#label_2{\n"
"font-size:8pt;\n"
"font-family:century gothic,bold;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{;\n"
"font: 10pt \"Impact\";\n"
"color:black;\n"
"\n"
"}\n"
"#frameAdd_2{\n"
"background-color:rgb(255,255,255)\n"
"}\n"
"#frame_4{\n"
"\n"
"background-color: rgb(0, 0, 0,32);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QLabel{\n"
"background:transparent;\n"
"}\n"
"#frame_8{\n"
"background:transparent;\n"
"border:1px solid black;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"#groupBox_7{\n"
"background:transparent;\n"
"border:1px solid black;\n"
"border-radius:8px\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border-bottom:2px solid  rgb(0,0,0,170);\n"
"border-radius:5px;\n"
"font-size:9pt;\n"
"font-family:century gothic;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(186, 186, 186);\n"
"}\n"
"#comboBox_3{\n"
"font-family:century gothic;\n"
"}\n"
"#pushmenuin1{\n"
"background-color: rgb(255, 255, 255,40);\n"
"}\n"
"\n"
"#pushmenuin1:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#pushAdd{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:5px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"color:white;\n"
"}\n"
"#pushAdd:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#pushAddpic{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:5px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"color:white;\n"
"}\n"
"#pushAddpic:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#pushtakephoto{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:5px;\n"
"border-bottom:3px solid rgb(104, 0, 0);\n"
"border-right:3px solid  rgb(104, 0, 0);\n"
"transition: all 1s;\n"
"color:white;\n"
"}\n"
"#pushtakephoto:hover{\n"
"background-color: rgb(255, 85, 0);\n"
"border-bottom:3px solid rgb(130, 43, 0);\n"
"border-right:3px solid rgb(130, 43, 0);\n"
"}\n"
"#textEdit{\n"
"border:1px solid black;\n"
"border-radius:8px;\n"
"font-size:9pt;\n"
"font-family:century gothic;\n"
"\n"
"}\n"
"#label_2{\n"
"font-size:8pt;\n"
"font-family:century gothic,bold;\n"
"\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(20, 10, 820, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(820, 460))
        self.frame_4.setStyleSheet("")
        self.frame_4.setObjectName("frame_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 250, 171, 41))
        self.groupBox_7.setStyleSheet("font: 9pt \"Arial Black\";")
        self.groupBox_7.setObjectName("groupBox_7")
        self.radioMale_3 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioMale_3.setGeometry(QtCore.QRect(10, 10, 50, 21))
        self.radioMale_3.setObjectName("radioMale_3")
        self.radioFemale_3 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioFemale_3.setGeometry(QtCore.QRect(80, 10, 71, 21))
        self.radioFemale_3.setObjectName("radioFemale_3")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setGeometry(QtCore.QRect(340, 270, 321, 201))
        self.frame_8.setStyleSheet("")
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_64 = QtWidgets.QLabel(self.frame_8)
        self.label_64.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_64.setObjectName("label_64")
        self.gridLayout_3.addWidget(self.label_64, 3, 0, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.frame_8)
        self.label_63.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_63.setObjectName("label_63")
        self.gridLayout_3.addWidget(self.label_63, 2, 0, 1, 1)
        self.lineGsis_3 = QtWidgets.QLineEdit(self.frame_8)
        self.lineGsis_3.setText("")
        self.lineGsis_3.setObjectName("lineGsis_3")
        self.gridLayout_3.addWidget(self.lineGsis_3, 2, 1, 1, 1)
        self.linePagibig_3 = QtWidgets.QLineEdit(self.frame_8)
        self.linePagibig_3.setText("")
        self.linePagibig_3.setObjectName("linePagibig_3")
        self.gridLayout_3.addWidget(self.linePagibig_3, 4, 1, 1, 1)
        self.lineSss_3 = QtWidgets.QLineEdit(self.frame_8)
        self.lineSss_3.setText("")
        self.lineSss_3.setObjectName("lineSss_3")
        self.gridLayout_3.addWidget(self.lineSss_3, 3, 1, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.frame_8)
        self.label_65.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_65.setObjectName("label_65")
        self.gridLayout_3.addWidget(self.label_65, 4, 0, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.frame_8)
        self.label_66.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_66.setObjectName("label_66")
        self.gridLayout_3.addWidget(self.label_66, 5, 0, 1, 1)
        self.linePhil_3 = QtWidgets.QLineEdit(self.frame_8)
        self.linePhil_3.setText("")
        self.linePhil_3.setObjectName("linePhil_3")
        self.gridLayout_3.addWidget(self.linePhil_3, 5, 1, 1, 1)
        self.pushAdd = QtWidgets.QPushButton(self.frame_8)
        self.pushAdd.setMinimumSize(QtCore.QSize(10, 0))
        self.pushAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushAdd.setStyleSheet("")
        self.pushAdd.setObjectName("pushAdd")
        self.gridLayout_3.addWidget(self.pushAdd, 6, 1, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.frame_8)
        self.label_67.setStyleSheet("font: 11pt \"Arial Black\";")
        self.label_67.setObjectName("label_67")
        self.gridLayout_3.addWidget(self.label_67, 0, 0, 1, 2)
        self.label_62 = QtWidgets.QLabel(self.frame_8)
        self.label_62.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_62.setObjectName("label_62")
        self.gridLayout_3.addWidget(self.label_62, 1, 0, 1, 1)
        self.lineTin_3 = QtWidgets.QLineEdit(self.frame_8)
        self.lineTin_3.setObjectName("lineTin_3")
        self.gridLayout_3.addWidget(self.lineTin_3, 1, 1, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 801, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_70 = QtWidgets.QLabel(self.layoutWidget)
        self.label_70.setStyleSheet("font: 12pt \"Arial Black\";")
        self.label_70.setObjectName("label_70")
        self.gridLayout_7.addWidget(self.label_70, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 80, 311, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_53 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_53.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_53.setObjectName("label_53")
        self.gridLayout_2.addWidget(self.label_53, 0, 0, 1, 1)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.layoutWidget1)
        self.dateEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_3.setStyleSheet("font: 10pt \"Century Gothic\";\n"
"font-color:black;")
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout_2.addWidget(self.dateEdit_3, 4, 1, 1, 1)
        self.lineFirstname_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineFirstname_3.setObjectName("lineFirstname_3")
        self.gridLayout_2.addWidget(self.lineFirstname_3, 0, 1, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_55.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 2, 0, 1, 1)
        self.lineLastname_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineLastname_3.setObjectName("lineLastname_3")
        self.gridLayout_2.addWidget(self.lineLastname_3, 2, 1, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_54.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_54.setObjectName("label_54")
        self.gridLayout_2.addWidget(self.label_54, 1, 0, 1, 1)
        self.lineMid_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineMid_3.setObjectName("lineMid_3")
        self.gridLayout_2.addWidget(self.lineMid_3, 1, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_72.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_72.setObjectName("label_72")
        self.gridLayout_2.addWidget(self.label_72, 3, 0, 1, 1)
        self.linePhone_9 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.linePhone_9.setObjectName("linePhone_9")
        self.gridLayout_2.addWidget(self.linePhone_9, 3, 1, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_56.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_56.setObjectName("label_56")
        self.gridLayout_2.addWidget(self.label_56, 4, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(345, 80, 311, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget2)
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit.setStyleSheet("font: 10pt \"Century Gothic\";\n"
"font-color: black;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_4.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_60.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_60.setObjectName("label_60")
        self.gridLayout_4.addWidget(self.label_60, 0, 0, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_73.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_73.setObjectName("label_73")
        self.gridLayout_4.addWidget(self.label_73, 1, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget2)
        self.dateEdit_2.setStyleSheet("font: 10pt \"Century Gothic\";\n"
"font-color:black;")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout_4.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.linePhone_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.linePhone_8.setObjectName("linePhone_8")
        self.gridLayout_4.addWidget(self.linePhone_8, 2, 1, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_71.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_71.setObjectName("label_71")
        self.gridLayout_4.addWidget(self.label_71, 2, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_68.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_68.setObjectName("label_68")
        self.gridLayout_4.addWidget(self.label_68, 4, 0, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_69.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_69.setObjectName("label_69")
        self.gridLayout_4.addWidget(self.label_69, 3, 0, 1, 1)
        self.linePhone_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.linePhone_7.setObjectName("linePhone_7")
        self.gridLayout_4.addWidget(self.linePhone_7, 3, 1, 1, 1)
        self.lineEmail_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEmail_3.setObjectName("lineEmail_3")
        self.gridLayout_4.addWidget(self.lineEmail_3, 4, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 300, 301, 151))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_58 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_58.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_58.setObjectName("label_58")
        self.gridLayout.addWidget(self.label_58, 1, 0, 1, 1)
        self.lineSalaryg_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineSalaryg_3.setObjectName("lineSalaryg_3")
        self.gridLayout.addWidget(self.lineSalaryg_3, 1, 1, 1, 1)
        self.lineDesignation_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineDesignation_3.setObjectName("lineDesignation_3")
        self.gridLayout.addWidget(self.lineDesignation_3, 0, 1, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_57.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 0, 0, 1, 1)
        self.lineStepincre_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineStepincre_3.setObjectName("lineStepincre_3")
        self.gridLayout.addWidget(self.lineStepincre_3, 2, 1, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_59.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_59.setObjectName("label_59")
        self.gridLayout.addWidget(self.label_59, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_3.setMinimumSize(QtCore.QSize(10, 0))
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 44, 44);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_61.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_61.setObjectName("label_61")
        self.gridLayout.addWidget(self.label_61, 3, 0, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(681, 70, 122, 404))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushbrowsepic = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushbrowsepic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushbrowsepic.setStyleSheet("font: 8pt \"Impact\";\n"
"color: rgb(255, 255, 255);")
        self.pushbrowsepic.setObjectName("pushbrowsepic")
        self.gridLayout_8.addWidget(self.pushbrowsepic, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        self.label.setMinimumSize(QtCore.QSize(120, 120))
        self.label.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(15, 5, 61, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\admin\\Desktop\\EID_final\\backbtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setGeometry(QtCore.QRect(90, 460, 231, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_74 = QtWidgets.QLabel(self.frame_4)
        self.label_74.setGeometry(QtCore.QRect(20, 460, 81, 20))
        self.label_74.setStyleSheet("font: 9pt \"Arial Black\";")
        self.label_74.setObjectName("label_74")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modify_Information"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Gender*"))
        self.radioMale_3.setText(_translate("MainWindow", "Male"))
        self.radioFemale_3.setText(_translate("MainWindow", "Female"))
        self.label_64.setText(_translate("MainWindow", "SSS*:"))
        self.label_63.setText(_translate("MainWindow", "GSIS*:"))
        self.lineGsis_3.setPlaceholderText(_translate("MainWindow", "Enter 11 digits only"))
        self.linePagibig_3.setPlaceholderText(_translate("MainWindow", "Enter 12 digits only"))
        self.lineSss_3.setPlaceholderText(_translate("MainWindow", "Enter 10 digits only"))
        self.label_65.setText(_translate("MainWindow", "PAGIBIG*:"))
        self.label_66.setText(_translate("MainWindow", "PHILHEALTH*:"))
        self.linePhil_3.setPlaceholderText(_translate("MainWindow", "Enter 12 digits only"))
        self.pushAdd.setText(_translate("MainWindow", "Modify"))
        self.label_67.setText(_translate("MainWindow", "Employee\'s Benefit Informations"))
        self.label_62.setText(_translate("MainWindow", "TIN*:"))
        self.lineTin_3.setPlaceholderText(_translate("MainWindow", "Enter 9 digits only"))
        self.label_70.setText(_translate("MainWindow", "Modify Employee\'s Personal Information"))
        self.label_2.setText(_translate("MainWindow", "note: all fields  that has  asterisk \'*\' should not leave empty"))
        self.label_53.setText(_translate("MainWindow", "First name*:"))
        self.dateEdit_3.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.lineFirstname_3.setPlaceholderText(_translate("MainWindow", "Firstname(i.e. RICARDO)"))
        self.label_55.setText(_translate("MainWindow", "Last name*:"))
        self.lineLastname_3.setPlaceholderText(_translate("MainWindow", "Last name (i.e. DALISAY)"))
        self.label_54.setText(_translate("MainWindow", "Middle name:"))
        self.lineMid_3.setPlaceholderText(_translate("MainWindow", "leave blank if No Middle name"))
        self.label_72.setText(_translate("MainWindow", "Item NO*:"))
        self.linePhone_9.setPlaceholderText(_translate("MainWindow", "numbers only"))
        self.label_56.setText(_translate("MainWindow", "Birthday*:"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.label_60.setText(_translate("MainWindow", "Date of Last Promotion*:"))
        self.label_73.setText(_translate("MainWindow", "First Day of Service*:"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.linePhone_8.setPlaceholderText(_translate("MainWindow", "Employee ID(numbers only)"))
        self.label_71.setText(_translate("MainWindow", "ID NO*:"))
        self.label_68.setText(_translate("MainWindow", "Email*:"))
        self.label_69.setText(_translate("MainWindow", "Phone Number*:"))
        self.linePhone_7.setPlaceholderText(_translate("MainWindow", "phone number(i.e.09............)"))
        self.lineEmail_3.setPlaceholderText(_translate("MainWindow", "email(i.e. abc123@....)"))
        self.label_58.setText(_translate("MainWindow", "Salary Grade*:"))
        self.lineSalaryg_3.setPlaceholderText(_translate("MainWindow", "Salary Grade(numbers only)"))
        self.lineDesignation_3.setPlaceholderText(_translate("MainWindow", "Designation(letters only)"))
        self.label_57.setText(_translate("MainWindow", "Designation*:"))
        self.lineStepincre_3.setPlaceholderText(_translate("MainWindow", "Step Increment(numbers only)"))
        self.label_59.setText(_translate("MainWindow", "Step Increment*:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "....."))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "TEACHING PERSONNEL"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "NON-TEACHING PERSONNEL"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "PART TIME"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "CONTRACT OF SERVICE"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "SEPARATED"))
        self.label_61.setText(_translate("MainWindow", "Employment Status*:"))
        self.pushbrowsepic.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "  2X2 Picture*"))
        self.pushButton.setToolTip(_translate("MainWindow", "Back to Main Page"))
        self.pushButton.setShortcut(_translate("MainWindow", "Esc"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "This field will only enabled if the employee status is \"Separated\""))
        self.label_74.setText(_translate("MainWindow", "Remarks:"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())