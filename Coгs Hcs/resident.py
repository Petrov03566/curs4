
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableView,QMessageBox, QWidget
from residentadd import AddResident
from delresident import Deleteresident



class ResidentAdd(AddResident):
    def __init__(self,flat):
        super().__init__()
        self.setupUi(self)
        self.flat=flat
        # self.lineEdit_data_bitch.setValidator(QtGui.QIntValidator())
        # self.lineEdit_fio_rt.setValidator(QtGui.QIntValidator())
        
        self.pb_add_resident.clicked.connect(self.add_resident1)
        self.pb_add_resident.clicked.connect(self.update_resident1)
        self.pushButton_cl_resident.clicked.connect(self.add_resident_cl)
        

    def add_resident1(self):
        if  len(self.lineEdit_fio_rt.text()) > 0 and len(self.lineEdit_pasport_data.text())> 0 and len(self.lineEdit_data_bitch.text())> 0 :
                query_rs = QSqlQuery()
                query_rs.exec(f"INSERT INTO public.resident(fIo_resident,pasport_data,date_birth,flat_id) VALUES('{self.lineEdit_fio_rt.text()}','{self.lineEdit_pasport_data.text()}','{self.lineEdit_data_bitch.text()}',{self.flat})")
                print(query_rs.lastError().text())
                self.close()

    def update_resident1(self):
        if  self.lineEdit_fio_rt.text() and self.lineEdit_pasport_data.text() and self.lineEdit_data_bitch.text():
                query_rs = QSqlQuery()
                query_rs.exec(f"UPDATE public.resident SET fIo_resident='{self.lineEdit_fio_rt.text()}', pasport_data='{self.lineEdit_pasport_data.text()}', data_bitch='{self.lineEdit_data_bitch.text()}'")
                print(query_rs.lastError().text())
                self.close()

    def add_resident_cl(self):
        self.close()

class DelResident(Deleteresident):
     def __init__(self):
        super().__init__()
        self.setupUi(self)


        