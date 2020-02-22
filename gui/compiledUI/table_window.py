from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt

class Ui_TableWindow(object):
    def setupUi(self, TableWindow):
        TableWindow.setObjectName("TableWindow")
        TableWindow.resize(566, 475)
        self.centralwidget = QtWidgets.QWidget(TableWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
            
        self.column_header = ['Book_ID','Title','Author','Category','ISBN','Publisher','Rack Number','Language']
        self.row = #need to be dynamic
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tableWidget.setWindowTitle("Transactional Data")
        self.tableWidget.setColumnCount(len(self.column_header))
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalHeaderLabels(self.column_header)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
       
        TableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        TableWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableWindow)
        self.statusbar.setObjectName("statusbar")
        TableWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(TableWindow)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        _translate = QtCore.QCoreApplication.translate
        TableWindow.setWindowTitle(_translate("LMS", "LMS"))
    
    #add -R- data to the table
    def insert(self, row, col, data):
        self.item = QTableWidgetItem(data)
        self.item.setFlags(self.item.flags() ^ Qt.ItemIsEditable)
        row-= row
        col-= col
        self.tableWidget.setItem(row,col,self.item)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TableWindow = QtWidgets.QMainWindow()
    ui = Ui_TableWindow()
    ui.setupUi(TableWindow)
    TableWindow.show()
    sys.exit(app.exec_())