from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery,QSqlQueryModel
from PyQt5.QtWidgets import QTableView,QMessageBox
from PyQt5 import QtGui
from addPaymen import AddPay
from delpay import Deletepay
from table import Ui_MainWindow

class PaymenAdd(AddPay):
    def __init__(self, flat,ParentWindow):
        super().__init__()
        self.setupUi(self)
        self.pb_add_pay1.clicked.connect(self.add_paymen)
        self.pushButton_cansel1.clicked.connect(lambda:self.close())
        self.flat_id = flat
        self.ParentWidget = ParentWindow
        # self.tableView_pay = QTableView(self.add_paymen)


    def add_paymen(self):
        row = self.ParentWidget.tableView_2.currentIndex().row()
        self.flat_id = self.ParentWidget.tableView_2.model().index(row, 0 ).data()
        if len(self.lineEdit_reporting_period.text()) > 0 and  len(self.lineEdit_4_cost.text()) > 0 and len(self.lineEdit_debt.text()) > 0 and len(self.lineEdit_data_pay.text()) > 0 and len(self.lineEdit_amount_paid.text()) > 0: 
            print(self.flat_id)
            queru_py =QSqlQuery()
            queru_py.exec(f"INSERT INTO public.payment (reporting_period,cost,debt,data_payment,amount_paid,flat_id) VALUES ('{self.lineEdit_reporting_period.text()}','{self.lineEdit_4_cost.text()}','{self.lineEdit_debt.text()}','{self.lineEdit_data_pay.text()}','{self.lineEdit_amount_paid.text()}', '{self.flat_id}')")
            print(queru_py.isActive())
            self.close()
    def update_paymen(self):
        if  self.lineEdit_reporting_period.text() and self.lineEdit_4_cost.text() and self.lineEdit_debt.text() and self.lineEdit_data_pay.text() and self.lineEdit_amount_paid():
                query_rs = QSqlQuery()
                query_rs.exec(f"UPDATE public.payment SET reporting_period='{self.lineEdit_reporting_period()}', cost='{self.lineEdit_4_cost.text()}', debt='{self.lineEdit_debt.text()}',data_payment='{self.lineEdit_data_pay}',amount_paid ='{self.lineEdit_amount_paid}'")
                print(query_rs.lastError().text())
                self.close()

        
class DelPay(Deletepay):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_no_pay.clicked.connect(self.cansel_dl_pay)

    def cansel_dl_pay(self):
        self.close()

   


    
    
        


        



