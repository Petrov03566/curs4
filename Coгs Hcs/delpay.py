from PyQt5 import QtCore, QtGui, QtWidgets


class Deletepay(QtWidgets.QMainWindow):
    def setupUi(self, Delete):
        Delete.setObjectName("Delete")
        Delete.resize(463, 145)
        self.label = QtWidgets.QLabel(Delete)
        self.label.setGeometry(QtCore.QRect(100, 10, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Delete)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 420, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_yes_pay = QtWidgets.QPushButton(Delete)
        self.pushButton_yes_pay.setGeometry(QtCore.QRect(20, 90, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_yes_pay.setFont(font)
        self.pushButton_yes_pay.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_yes_pay.setObjectName("pushButton_yes_pay")
        self.pushButton_no_pay = QtWidgets.QPushButton(Delete)
        self.pushButton_no_pay.setGeometry(QtCore.QRect(360, 90, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_no_pay.setFont(font)
        self.pushButton_no_pay.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_no_pay.setObjectName("pushButton_no_pay")

        self.retranslateUi(Delete)
        QtCore.QMetaObject.connectSlotsByName(Delete)

    def retranslateUi(self, Delete):
        _translate = QtCore.QCoreApplication.translate
        Delete.setWindowTitle(_translate("Delete", "удаление строки"))
        self.label_2.setText(_translate("Delete", "Вы хотите удалить это строчку?"))
        self.pushButton_yes_pay.setText(_translate("Delete", "да "))
        self.pushButton_no_pay.setText(_translate("Delete", "нет"))
