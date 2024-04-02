from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QTableView,QMessageBox
from PyQt5 import QtGui
from flatWindow import FlatWindow
from Delflat import Deleteflat

class FlatAdd(FlatWindow):
    def __init__(self, setTable):
        super().__init__(True)
        self.lineEdit_square_flat.setValidator(QtGui.QIntValidator())
        self.lineEdit_quantity_residents.setValidator(QtGui.QIntValidator())
        self.setTable = setTable
        self.pushButton_yes_flat.clicked.connect(self.add_flat)
        self.pushButton_cl_flat.clicked.connect(lambda: self.close())
        
    
    def add_flat(self):
        if len(self.lineEdit_square_flat.text()) > 0 and len(self.lineEdit_quantity_residents.text()) > 0 and len(self.lineEdit_adress_flat.text()) > 0:
            availability = 0
            if self.checkBox.isChecked():
                availability = 1
            query_ft = QSqlQuery()
            query_ft.exec(f"INSERT INTO public.flat(square_flat, quantity_residents, availability_benefits, address) VALUES ('{self.lineEdit_square_flat.text()}','{self.lineEdit_quantity_residents.text()}','{availability}','{self.lineEdit_adress_flat.text()}')")
            print(query_ft.isActive())
            self.setTable()
            self.close()

class FlatChange(FlatWindow):
    def __init__(self, setTable, id: int):
        super().__init__(False)
        self.id = id
        self.lineEdit_square_flat.setValidator(QtGui.QIntValidator())
        self.lineEdit_quantity_residents.setValidator(QtGui.QIntValidator())
        self.setTable = setTable
        self.pushButton_yes_flat.clicked.connect(self.add_flat)
        self.pushButton_cl_flat.clicked.connect(lambda: self.close())
    
    def add_flat(self):
        availability = 0
        if self.checkBox.isChecked():
            availability = 1
        query_ft = QSqlQuery()
        query_ft.exec(f"UPDATE public.flat SET square_flat = '{self.lineEdit_square_flat.text()}', quantity_residents ='{self.lineEdit_quantity_residents.text()}' , availability_benefits ='{availability}' , address= '{self.lineEdit_adress_flat.text()}'")
        print(query_ft.isActive())
        self.setTable()
        self.close()

class DeleteFlat(Deleteflat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pb_yes_flat.clicked.connect()