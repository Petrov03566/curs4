from PyQt5 import *
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import main1
from add_flat import Add_Flat_window
import add_pay

class HcsWindow(main1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton_flat_add.clicked.connect(self.add_flat_button)
        self.pushButton_Pay_add.clicked.connect(self.add_pay_button)
        self.current_dep = 0
        self.pushButton_flat_add.clicked.connect(self.add_flat_button)
        self.pushButton_Pay_add.clicked.connect(self.add_pay_button)

  
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('Hcs')
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        self.update_flat()

        query = QSqlTableModel()
        sql = "SELECT * FROM public.flat"
        query.setTable("flat")
        query.select()
        self.tableView_Flat.setModel(query)

        query = QSqlTableModel()
        sql = "SELECT * FROM public.payment"
        query.setTable("payment")
        query.select()
        self.tableView_Pay.setModel(query)

        query = QSqlTableModel()
        sql = "SELECT * FROM public.resident"
        query.setTable("resident")
        query.select()
        self.tableView_Resident.setModel(query)

    def add_flat_button(self):
        self.add_f = Add_Flat_window(self.update_flat)
        self.add_f.show()

    def add_pay_button(self):
        self.add_p =Add_Pay(self.update_flat)
        self.add_p.show()
    

    # def add_Ward_Button(self):
    #     self.add_w = Add_Ward(self.current_dep, self.update_dep)
    #     self.add_w.show()

    def dp_clicked(self):
        row = self.tableView_Flat.selectedIndexes()[0].row()
        self.current_dep = self.tableView_Flat.model().index(row, 0).data()

    def update_flat(self):
        query = QSqlTableModel()
        query.setTable("flat")
        query.select()
        self.tableView_Flat.setModel(query)

class Add_Flat(Add_Flat_window.Ui_MainWindow):
    def __init__(self, update_dep):
        super().__init__()
        self.setupUi(self)

        self.update_dep = update_dep

        self.pushButton_add_base_Flat.clicked.connect(self.add_b_flat)
        self.pushButton_exit_Flat.clicked.connect(self.exit_flat)

    def exit_flat(self):
        self.close()

    def add_b_flat(self):
        query = QSqlQuery()
        query.exec(f"INSERT INTO public.flat (square_flat,quantity_residents,availability_benefits,address) VALUES ('{self.lineEdit_add_Flat_square.text()}', '{self.lineEdit_2_add_Flat_quanity_resident.text()}','{self.lineEdit_add_availability_benefits.text()}','{self.lineEdit_add_Flat_adress.text()}')")
        self.update_dep()

class Add_Pay(add_pay.Ui_MainWindow):
    def __init__(self, dep_id, update_dep):
        super().__init__()
        self.setupUi(self)

        self.dep_id = dep_id
        self.update_dep = update_dep

        self.pushButton_exit_Pay.clicked.connect(self.exit_pay)
        self.pushButton_add_Pay.clicked.connect(self.add_w_pay)

    def exit_pay(self):
        self.close()

    def add_w_pay(self):
        query = QSqlQuery()
        query.exec(f"INSERT INTO public.pay(reporting_period, cost, debt,data_payment,amount_paid,flat_id) VALUES ('{self.lineEdit_add_reporting_period.text()}', '{self.lineEdit_2_add_cost.text()}',{self.lineEdit_add_debt.text()}, '{self.lineEdit_add_amount_paid.text()}')")
        self.update_dep()
        
app = QApplication(sys.argv)
window = HcsWindow()
window.show()
app.exec()