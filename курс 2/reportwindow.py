from report import ReportWindow
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Report(ReportWindow):
    def __init__(self, row1, col):
        super().__init__()
        self.setupUi(self)
        self.date_start = ''
        self.date_end = ''
        self.create_btn.clicked.connect(self.btn_clicked)
        self.print_btn.clicked.connect(self.print_btn_clicked)
        self.start_dateEdit.setDate(QtCore.QDate.currentDate())
        self.start_dateEdit.setDisplayFormat("yyyy-MM-dd") 
        self.end_dateEdit.setDate(QtCore.QDate.currentDate())
        self.end_dateEdit.setDisplayFormat("yyyy-MM-dd")
        
        
    def btn_clicked(self):
        self.date_start = f"{self.start_dateEdit.date().year()}.{self.start_dateEdit.date().month()}.{self.start_dateEdit.date().day()}"
        self.date_end = f"{self.end_dateEdit.date().year()}.{self.end_dateEdit.date().month()}.{self.end_dateEdit.date().day()}"
        self.set_table(self.date_start, self.date_end)
        self.subtitle_lbl.setText(f"об информации о рейсах за период с {self.date_start} по {self.date_end}")
    
    def print_btn_clicked(self):
        if len(self.date_start) > 0 and len(self.date_end) > 0:
            self.dialog = QtPrintSupport.QPrintDialog()
            if self.dialog.exec_() == 1:
                textDoc = QtGui.QTextDocument()
                html = self.build_document()
                textDoc.setHtml(html)
                printer = self.dialog.printer()
                textDoc.print(printer)
        else:
            QtWidgets.QMessageBox.warning(self, "Внимание", "Вы не сформировли отчет")
            
    def set_table(self, date_start, date_end):
        query = QSqlQueryModel()
        query.setQuery(f"SELECT public.flights.number_flights, station, timeout, public.wagons.number_wagons, type, place, price, public.tickets.date, sold_ticket FROM public.flights INNER JOIN public.wagons ON public.flights.number_flights = public.wagons.number_flights INNER JOIN public.tickets ON public.wagons.number_wagons = public.tickets.number_wagons WHERE public.tickets.date BETWEEN '{date_start}' AND '{date_end}'")
        self.tableView.setModel(query)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(7, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(8, QHeaderView.Stretch)
        query.setHeaderData(0, QtCore.Qt.Horizontal, "Номер рейса")
        query.setHeaderData(1, QtCore.Qt.Horizontal, "Станция назначения")
        query.setHeaderData(2, QtCore.Qt.Horizontal, "Время отправления")
        query.setHeaderData(3, QtCore.Qt.Horizontal, "Номер вагона")
        query.setHeaderData(4, QtCore.Qt.Horizontal, "Тип")
        query.setHeaderData(5, QtCore.Qt.Horizontal, "Количество мест")        
        query.setHeaderData(6, QtCore.Qt.Horizontal, "Цена")
        query.setHeaderData(7, QtCore.Qt.Horizontal, "Дата")
        query.setHeaderData(8, QtCore.Qt.Horizontal, "Проданные билеты")
        
        
        
    def build_document(self):
        html = f"""<h1 style ='text-align:center;'>Отчет</h1>
        <h3 style = 'text-align:center; margin-bottom: 100px'>О рейсах за период с {self.date_start} по {self.date_end}</h3>
        <table style = 'text-align: center; margin-left:10%; border-collapse: collapse;'>
        </thead>
            <tr>
                <th style = 'border: 1px solid black; width: 100px;'>Номер рейса</th>
                <th style = 'border: 1px solid black; width: 100px;'>Станция</th>
                <th style = 'border: 1px solid black; width: 100px;'>Время отправления</th>
                <th style = 'border: 1px solid black; width: 100px;'>Номер вагона</th>
                <th style = 'border: 1px solid black; width: 100px;'>Тип</th>
                <th style = 'border: 1px solid black; width: 100px;'>Количество мест</th>
                <th style = 'border: 1px solid black; width: 100px;'>Цена (р)</th>
                <th style = 'border: 1px solid black; width: 100px;'>Дата</th>
                <th style = 'border: 1px solid black; width: 100px;'>Колличество проданных билетов</th>
            </tr>
        </thead>
        </tbody>"""
        model = self.tableView.model()
        row_count = model.rowCount()
        column_count = model.columnCount()
        
        for row in range(row_count):
            html += "<tr>"
            for column in range(column_count):
                index = model.index(row,column)
                data = model.data(index)
                if isinstance(data, QDate):
                    data = data.toString("yyyy/MM/dd")
                html += f"<td style = 'border: 1px solid black; width: 100px;'>{data}</td>"
            html += "</tr>"
            
        html += "</tbody><table>"
        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertHtml(html)
        return document.toHtml()
