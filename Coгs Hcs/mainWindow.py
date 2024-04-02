import sys
from table import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QHeaderView
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel,QSqlTableModel
from pay import PaymenAdd,DelPay
from flat import FlatAdd, FlatChange,DeleteFlat
from resident import ResidentAdd,DelResident

class HcmWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currentFlat = 0
        self.db_connection()
        self.pushButton_add_pay.clicked.connect(self.add_pay)
        self.pb_add_flat.clicked.connect(self.add_flat)
        self.pb_add_habitation.clicked.connect(self.add_resident)
        self.pb_change2.clicked.connect(self.change_flat)

        self.tableView_2.clicked.connect(self.flat_cellClicked)
        self.pushButton_delete_pay.clicked.connect(self.delete_pay)
        self.pb_delete3.clicked.connect(self.delete_resident)
        self.pb_delete2.clicked.connect(self.delete_flat)
        self.tableView_2.clicked.connect(self.btn_table)
        self.flat_id =0
    
    def add_pay(self):
        self.Pay = PaymenAdd(self.flat_id)
        self.Pay.show()

    def add_resident(self):
        self.resident = ResidentAdd(self.setFlat, self)
        self.resident.show()
    def add_flat(self):
        self.Flat = FlatAdd(self.setFlat)
        self.Flat.show()
    
    def delete_resident(self):
        self.Flat = DelResident()
        self.Flat.show()
    
    def delete_pay(self):
        self.Pay = DelPay()
        self.Pay.show()
    def delete_flat(self):
        self.Flat = DeleteFlat()
        self.Flat.show()

    def change_flat(self):
        self.Flat = FlatChange(self.setFlat, id = self.currentFlat)
        self.Flat.show()

    # def delete_pay(self):
    #     self.DeletePay =DeleteKey()
    #     self.DeletePay.show()
    
    def flat_cellClicked(self):
        row = self.tableView_2.selectedIndexes()[0].row()
        self.currentFlat = self.tableView_2.model().index(row, 0).data()
   
    
    def db_connection(self):
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("student")
        db.setPort(5432)
        db.setDatabaseName("Hcs")
        db.setHostName("localhost")
        db.open()
#база данных 
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM public.payment")
        self.tableView_pay.setModel(query)
        self.tableView_pay.hideColumn(0)
        stm =QSqlTableModel()
        stm.setTable('payment')
        stm.select()
        self.tableView_pay.setModel(stm)
        stm.setHeaderData(1, QtCore.Qt.Horizontal, "Отчетный период")
        stm.setHeaderData(2, QtCore.Qt.Horizontal,"стоимость")
        stm.setHeaderData(3, QtCore.Qt.Horizontal,"долг")
        stm.setHeaderData(4, QtCore.Qt.Horizontal, "дата оплаты")
        stm.setHeaderData(5, QtCore.Qt.Horizontal, "оплаченная сумма")
        self.tableView_pay.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
       

        self.setFlat()
        
        query3 =QSqlQueryModel()
        query3.setQuery("SELECT * FROM public.resident")
        self.tableView_3.setModel(query3)
        self.tableView_3.hideColumn(0)
        stm2 =QSqlTableModel()
        stm2.setTable("resident")
        stm2.select()
        self.tableView_3.setModel(stm2)
        stm2.setHeaderData(1, QtCore.Qt.Horizontal, "код проживающих")
        stm2.setHeaderData(2, QtCore.Qt.Horizontal,"ФИО проживающих")
        stm2.setHeaderData(3, QtCore.Qt.Horizontal, "паспортные данные")
        stm2.setHeaderData(4, QtCore.Qt.Horizontal, "дата рождения")
        self.tableView_pay.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
   
       
    def setFlat(self):
        query =QSqlQueryModel()
        query.setQuery("SELECT * FROM public.flat")
        self.tableView_2.setModel(query)
        self.tableView_2.hideColumn(0)
        stm3 =QSqlTableModel()
        stm3.setTable("flat")
        stm3.select()
        self.tableView_2.setModel(stm3)
        stm3.setHeaderData(1, QtCore.Qt.Horizontal, "площадь квартиры")
        stm3.setHeaderData(2, QtCore.Qt.Horizontal,"количество проживающих")
        stm3.setHeaderData(3, QtCore.Qt.Horizontal,"наличие льготы")
        stm3.setHeaderData(4, QtCore.Qt.Horizontal,"Адрес")
        self.tableView_pay.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tableView_pay.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        

   
    def btn_table(self):
        row = self.tableView_2.currentIndex().row()
        self.flat_id = self.tableView_2.model().index(row, 0 ).data()

app =QApplication(sys.argv)
window = HcmWindow()
window.show()
app.exec()