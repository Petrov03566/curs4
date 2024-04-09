from PyQt5 import *
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import main1
import add_flat 
import add_pay
import add_resident
import DeleteFlat

class HcsWindow(main1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.current_flat = 0
        self.current_pay = 0
        self.current_resident=0


        self.pushButton_flat_remove.clicked.connect(self.chance_flat)
        self.pushButton_Resident_remove.clicked.connect(self.chance_resident)
        self.pushButton_Pay_remove.clicked.connect(self.chance_pay)
        self.pushButton_flat_add.clicked.connect(self.add_flat_button)
        self.pushButton_flat_delete.clicked.connect(self.delete_flat)
        self.pushButton_Pay_delete.clicked.connect(self.delete_pay)
        self.pushButton_Resident_delete.clicked.connect(self.delete_resident)
        self.pushButton_Pay_add.clicked.connect(self.add_pay_button)
        self.pushButton_Resident_add.clicked.connect(self.add_resident_button)
        self.tableView_Flat.clicked.connect(self.fl_clicked)
        self.tableView_Pay.clicked.connect(self.pay_clicked)
  
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('Hcs')
        db.setUserName('postgres')
        db.setPassword('Doctor')
        db.open()

        self.update_flat()
        self.update_payment()
        self.update_resident()
    
        query = QSqlTableModel()
        sql = "SELECT * FROM public.flat"
        query.setTable("flat")
        query.select()
        self.tableView_Flat.setModel(query)
        self.current_flat = self.tableView_Flat.model().index(0, 0).data()

        query = QSqlTableModel()
        sql = "SELECT * FROM public.payment"
        query.setTable("payment")
        query.select()

        self.tableView_Pay.setModel(query)
        self.current_flat = self.tableView_Flat.model().index(0, 0).data()
        query = QSqlTableModel()
        sql = "SELECT * FROM public.resident"
        query.setTable("resident")
        query.select()

        self.tableView_Resident.setModel(query)
        self.current_flat = self.tableView_Flat.model().index(0, 0).data()
    
    def add_flat_button(self):
        self.add_f =Flat(self.update_flat, 1, self.current_flat)
        self.add_f.show()

    def chance_flat(self):
        self.add_f =Flat(self.update_flat,2,self.current_flat)
        self.add_f.show()
    def add_cl_flat(self):
        self.add_f.close()

    def add_pay_button(self):
        self.add_p =Pay(self.current_flat,self.update_payment, 1 ,self.current_pay)
        self.add_p.show()

    def chance_pay(self):
        self.add_p =Pay(self.current_flat, self.update_payment, 2,self.current_pay)
        self.add_p.show()

    def add_resident_button(self):
        self.add_r = Resident(self.current_flat,self.update_resident, 1, self.current_resident)
        self.add_r.show()

    def chance_resident(self):
        self.add_r =Resident(self.current_resident,self.update_resident,2,self.current_resident)
        self.add_r.show()

    def fl_clicked(self):
        row = self.tableView_Flat.selectedIndexes()[0].row()
        self.current_flat = self.tableView_Flat.model().index(row, 0).data()
    
    def pay_clicked(self):  
        row = self.tableView_Pay.selectedIndexes()[0].row()
        self.current_flat= self.tableView_Pay.model().index(row, 0).data()
    
    def resident_clicked(self):
        row = self.tableView_Resident.selectedIndexes()[0].row()
        self.curent_procedure = self.tableView_Resident.model().index(row, 0).data()


    def update_flat(self):
        query = QSqlTableModel()
        query.setTable("flat")
        query.select()
        self.tableView_Flat.setModel(query)

    def update_payment(self):
        query = QSqlTableModel()
        query.setTable("payment")
        query.select()
        self.tableView_Pay.setModel(query)

    def update_resident(self):
        query = QSqlTableModel()
        query.setTable("resident")
        query.select()
        self.tableView_Resident.setModel(query)

    def delete_flat(self):
        flt = QMessageBox()
        flt.setWindowTitle("Внимание")
        flt.setText("Вы действительно хотите удалить данные? Данные будут безвозвратно удалены.")
        flt.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        button = flt.exec()
        if button == QMessageBox.StandardButton.Ok:
            query = QSqlQuery()
            query.exec(f"DELETE FROM public.flat WHERE id = '{self.current_flat}'")
            self.update_flat()
        else:
            flt.close()

    def delete_pay(self):
        paymt = QMessageBox()
        paymt.setWindowTitle("Внимание")
        paymt.setText("Вы действительно хотите удалить данные? Данные будут безвозвратно удалены.")
        paymt.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        button = paymt.exec()
        if button == QMessageBox.StandardButton.Ok:
            query = QSqlQuery()
            query.exec(f"DELETE FROM public.pay WHERE id = '{self.current_pay}'")
            self.update_payment()
        else:
            paymt.close()

    def delete_resident(self):
        rdt= QMessageBox()
        rdt.setWindowTitle("Внимание")
        rdt.setText("Вы действительно хотите удалить данные? Данные будут безвозвратно удалены.")
        rdt.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        button = rdt.exec()
        if button == QMessageBox.StandardButton.Ok:
            query = QSqlQuery()
            query.exec(f"DELETE FROM public.resident WHERE id = '{self.current_resident}'")
            self.update_resident()
        else:
            rdt.close()


# #Конец основного окна

class Flat(add_flat.Ui_MainWindow):
    def __init__(self, update_flat,current_flat,chance_fl):
        super().__init__()
        self.setupUi(self)

        self.update_flat = update_flat
        self.chance_fl = chance_fl
        self.current_flat= current_flat
        self.pushButton_add_base_Flat.clicked.connect(self.add_f_flat)
        self.pushButton_exit_Flat.clicked.connect(self.exit_flat)
        
    def exit_flat(self):
        self.close()

    def add_f_flat(self):
        if self.chance_fl ==1:
            query = QSqlQuery()
            query.exec(f"INSERT INTO public.flat(square_flat,quantity_residents,availability_benefits,address) VALUES ('{self.lineEdit_add_Flat_square.text()}', '{self.lineEdit_2_add_Flat_quanity_resident.text()}','{self.lineEdit_add_availability_benefits.text()}','{self.lineEdit_add_Flat_adress.text()}')")
            self.update_flat()
        elif self.chance_fl == 2:
            query = QSqlQuery()
            query.exec(f"UPDATE public.flat SET square_falt ='{self.lineEdit_add_Flat_square}',quantity_residents='{self.lineEdit_2_add_Flat_quanity_resident}',availability_benefits='{self.lineEdit_add_availability_benefits}',address='{self.lineEdit_add_Flat_adress}'")
            self.update_flat()
    



class Pay(add_pay.Ui_MainWindow):
    def __init__(self, flat_id,update_pay,chance_pay):
        super().__init__()
        self.setupUi(self)

        self.flat_id = flat_id
        self.update_pay = update_pay
        self.chance_pay = chance_pay
        self.pushButton_exit_Pay.clicked.connect(self.exit_pay)
        self.pushButton_add_Pay.clicked.connect(self.add_p_pay)

    def exit_pay(self):
        self.close()

    def add_p_pay(self):
        if self.chance_pay ==1:
            query = QSqlQuery()
            SQL = f"INSERT INTO public.payment(reporting_period, cost, debt,data_payment,amount_paid,flat_id) VALUES (" + \
                    f"{self.lineEdit_add_reporting_period.text()}, {self.lineEdit_2_add_cost.text()},{self.lineEdit_add_debt.text()}, '{self.dateEdit_data_payment.text()}'," + \
                    f"{self.lineEdit_add_amount_paid.text()}, {self.flat_id})"
            query.exec(SQL)
            self.update_pay()
        elif self.chance_pay==2:
            query= QSqlQuery()
            query.exec(f"UPDATE public.resident reporting_period ='{self.lineEdit_add_reporting_period}',cost ='{self.lineEdit_2_add_cost}',debt='{self.lineEdit_add_debt}',data_payment='{self.dateEdit_data_payment}',amount_paid ='{self.lineEdit_add_amount_paid}'WHERE id ='{self.flat_id}")
            self.update_pay()

    
        self.update_pay()

class Resident(add_resident.Ui_MainWindow):
    def __init__(self, flat_id,update_resident,chance_rs):
        super().__init__()
        self.setupUi(self)


        self.flat_id =flat_id
        self.update_resident= update_resident
        self.chance_rs =chance_rs

        self.flat_id=flat_id
        self.update_resident =update_resident
        self.pushButton_add_base_Resident.clicked.connect(self.add_resident)
        self.pushButton_exit_Resident.clicked.connect(self.exit_resident)
    
    def exit_resident(self):
        self.close()

    def add_resident(self):
        if self.chance_rs ==1:
            query =QSqlQuery()
            query.exec(f"INSERT INTO public.resident(fio_resident,pasport_data,date_birth,flat_id) VALUES('{self.lineEdit_2_add_Resident_fio_resident.text()}','{self.lineEdit_add_resident_pasport_data.text()}','{self.dateEdit_date_nitch.text()}','{self.flat_id}')")
            self.update_resident()
        elif self.chance_rs==2:
            query =QSqlQuery()
            query.exec(F"UPDATE public.resident SET fio_resident ='{self.lineEdit_2_add_Resident_fio_resident}',pasport_data='{self.lineEdit_add_resident_pasport_data}',data_bitch ='{self.dateEdit_date_nitch}'WHERE id = {self.flat_id}")
            self.update_resident()

app = QApplication(sys.argv)
window = HcsWindow()
window.show()
app.exec()