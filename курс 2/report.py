from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class ReportWindow(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1182, 768)
        self.title_lbl = QtWidgets.QLabel(Form)
        self.title_lbl.setGeometry(QtCore.QRect(540, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")
        self.start_date_lbl = QtWidgets.QLabel(Form)
        self.start_date_lbl.setGeometry(QtCore.QRect(60, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_date_lbl.setFont(font)
        self.start_date_lbl.setObjectName("start_date_lbl")
        self.start_dateEdit = QtWidgets.QDateEdit(Form)
        self.start_dateEdit.setGeometry(QtCore.QRect(220, 10, 121, 31))
        self.start_dateEdit.setObjectName("start_dateEdit")
        self.end_dateEdit = QtWidgets.QDateEdit(Form)
        self.end_dateEdit.setGeometry(QtCore.QRect(530, 10, 121, 31))
        self.end_dateEdit.setObjectName("end_dateEdit")
        self.end_date_lbl = QtWidgets.QLabel(Form)
        self.end_date_lbl.setGeometry(QtCore.QRect(380, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.end_date_lbl.setFont(font)
        self.end_date_lbl.setObjectName("end_date_lbl")
        self.create_btn = QtWidgets.QPushButton(Form)
        self.create_btn.setGeometry(QtCore.QRect(730, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.create_btn.setFont(font)
        self.create_btn.setStyleSheet("QPushButton{\n"
"border-radius: 9px;\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 9px;\n"
"border: 2px solid black;\n"
"background-color: rgb(246, 245, 244);\n"
"}")
        self.create_btn.setObjectName("create_btn")
        self.print_btn = QtWidgets.QPushButton(Form)
        self.print_btn.setGeometry(QtCore.QRect(900, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet("QPushButton{\n"
"border-radius: 9px;\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 9px;\n"
"border: 2px solid black;\n"
"background-color: rgb(246, 245, 244);\n"
"}")
        self.print_btn.setObjectName("print_btn")
        self.subtitle_lbl = QtWidgets.QLabel(Form)
        self.subtitle_lbl.setGeometry(QtCore.QRect(290, 100, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.subtitle_lbl.setFont(font)
        self.subtitle_lbl.setText("")
        self.subtitle_lbl.setObjectName("subtitle_lbl")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 140, 1161, 611))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Отчет"))
        self.title_lbl.setText(_translate("Form", "Отчет"))
        self.start_date_lbl.setText(_translate("Form", "Начальная дата"))
        self.end_date_lbl.setText(_translate("Form", "Конечная дата"))
        self.create_btn.setText(_translate("Form", "Сформировать"))
        self.print_btn.setText(_translate("Form", "Печать"))
