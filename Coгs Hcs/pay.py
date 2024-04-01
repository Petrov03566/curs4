from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery,QSqlQueryModel
from PyQt5.QtWidgets import QTableView,QMessageBox
from PyQt5 import QtGui
from addPaymen import AddPay
from delpay import Deletepay

class PaymenAdd(AddPay):
    def __init__(self, flat):
        super().__init__()
        self.setupUi(self)
        self.pb_add_pay1.clicked.connect(self.add_paymen)
        self.pushButton_cansel1.clicked.connect(lambda:self.close())
        self.flat_id = flat
        # self.tableView_pay = QTableView(self.add_paymen)


    def add_paymen(self):
        if len(self.lineEdit_reporting_period.text()) > 0 and  len(self.lineEdit_4_cost.text()) > 0 and len(self.lineEdit_debt.text()) > 0 and len(self.lineEdit_data_pay.text()) > 0 and len(self.lineEdit_amount_paid.text()) > 0: 
            print(self.flat_id)
            queru_py =QSqlQuery()
            queru_py.exec(f"INSERT INTO public.payment (reporting_period,cost,debt,data_payment,amount_paid,flat_id) VALUES ('{self.lineEdit_reporting_period.text()}','{self.lineEdit_4_cost.text()}','{self.lineEdit_debt.text()}','{self.lineEdit_data_pay.text()}','{self.lineEdit_amount_paid.text()}', '{self.flat_id}')")
            print(queru_py.isActive())
            self.close()
            # print(queru_py.lastError().text())
            
            # queru_py.setQuery("SELECT * FROM public.payment")
            # self.tableView_pay.setModel(queru_py)
            # self.close()

class DelPay(Deletepay):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

   


    
    
        


        



