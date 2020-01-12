from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_popUp_account_created_Window(object):
    def setupUi(self, popUp_account_created_Window):
        popUp_account_created_Window.setObjectName("popUp_account_created_Window")
        popUp_account_created_Window.resize(275, 125)
        self.centralwidget = QtWidgets.QWidget(popUp_account_created_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 90))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.text_label2 = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_label2.setFont(font)
        self.text_label2.setObjectName("text_label2")
        self.gridLayout.addWidget(self.text_label2, 2, 0, 1, 1)
        self.text_label = QtWidgets.QLabel(self.gridLayoutWidget)
       
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_label.setFont(font)
        self.text_label.setObjectName("text_label")
        self.gridLayout.addWidget(self.text_label, 1, 0, 1, 1)
        popUp_account_created_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(popUp_account_created_Window)
        self.statusbar.setObjectName("statusbar")
        popUp_account_created_Window.setStatusBar(self.statusbar)

        self.retranslateUi(popUp_account_created_Window)
        QtCore.QMetaObject.connectSlotsByName(popUp_account_created_Window)

        
        

    def retranslateUi(self, popUp_account_created_Window):
        _translate = QtCore.QCoreApplication.translate
        popUp_account_created_Window.setWindowTitle(_translate("popUp_account_created_Window", "msg"))
        self.text_label2.setText(_translate("popUp_account_created_Window", "account is now valid!"))
        self.text_label.setText(_translate("popUp_account_created_Window", "Account Created! 🎉"))

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            quit.triggered.connect(self.close)
        else:
            event.ignore()

        time.sleep(10)
        self.closeEvent(self)