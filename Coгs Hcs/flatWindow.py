from PyQt5 import QtCore, QtGui, QtWidgets


class FlatWindow(QtWidgets.QWidget):
    def __init__(self, isAdd: bool = True):
        super().__init__()
        self.setupUi(self)
        if isAdd == True:
            self.pushButton_yes_flat.setText("Добавить")
        else:
            self.pushButton_yes_flat.setText("Изменить")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(375, 326)
        self.label_address = QtWidgets.QLabel(Form)
        self.label_address.setGeometry(QtCore.QRect(120, 10, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_address.setFont(font)
        self.label_address.setObjectName("label_address")
        self.lineEdit_adress_flat = QtWidgets.QLineEdit(Form)
        self.lineEdit_adress_flat.setGeometry(QtCore.QRect(10, 50, 340, 30))
        self.lineEdit_adress_flat.setObjectName("lineEdit_adress_flat")
        self.label_square_flat = QtWidgets.QLabel(Form)
        self.label_square_flat.setGeometry(QtCore.QRect(50, 80, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_square_flat.setFont(font)
        self.label_square_flat.setObjectName("label_square_flat")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 340, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_square_flat = QtWidgets.QLineEdit(Form)
        self.lineEdit_square_flat.setGeometry(QtCore.QRect(10, 130, 340, 30))
        self.lineEdit_square_flat.setObjectName("lineEdit_square_flat")
        self.lineEdit_quantity_residents = QtWidgets.QLineEdit(Form)
        self.lineEdit_quantity_residents.setGeometry(QtCore.QRect(10, 200, 340, 30))
        self.lineEdit_quantity_residents.setObjectName("lineEdit_quantity_residents")
        self.pushButton_yes_flat = QtWidgets.QPushButton(Form)
        self.pushButton_yes_flat.setGeometry(QtCore.QRect(20, 280, 100, 30))
        self.pushButton_yes_flat.setObjectName("pushButton_yes_flat")
        self.pushButton_cl_flat = QtWidgets.QPushButton(Form)
        self.pushButton_cl_flat.setGeometry(QtCore.QRect(250, 280, 90, 30))
        self.pushButton_cl_flat.setObjectName("pushButton_cl_flat")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 240, 241, 24))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить квартиру"))
        self.label_address.setText(_translate("Form", "Адрес"))
        self.label_square_flat.setText(_translate("Form", "Площадь квартиры "))
        self.label_3.setText(_translate("Form", "количество проживающих "))
        self.pushButton_yes_flat.setText(_translate("Form", "добавить "))
        self.pushButton_cl_flat.setText(_translate("Form", "отмена "))
        self.checkBox.setText(_translate("Form", "Наличие льготы"))
