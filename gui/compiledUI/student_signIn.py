from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from compiledUI.account_created import *
import os
import json
import sqlite3

class Ui_SignInWindow(object):


    def openPopUpWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_popUp_account_created_Window()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def popWindow(self):
        msg = QMessageBox()
        msg.setWindowTitle("Congratz")
        msg.setText("Account Created! 🎉")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Close)
        exe = msg.exec_()

    def setupUi(self, SignInWindow):
        SignInWindow.setObjectName("SignInWindow")
        SignInWindow.resize(365, 300)
        self.centralwidget = QtWidgets.QWidget(SignInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 301, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 3, 0, 1, 1)
        self.email_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 3, 1, 1, 1)
        self.level_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.level_label.setFont(font)
        self.level_label.setObjectName("level_label")
        self.gridLayout.addWidget(self.level_label, 1, 0, 1, 1)
        self.email_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_input.setObjectName("email_input")
        self.gridLayout.addWidget(self.email_input, 2, 1, 1, 1)
        self.name_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 0, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.level_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.level_input.setObjectName("level_input")
        self.gridLayout.addWidget(self.level_input, 1, 1, 1, 1)
        self.submit = QtWidgets.QPushButton(self.gridLayoutWidget, enabled = False)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 4, 1, 1, 1)
        self.signInForum_label = QtWidgets.QLabel(self.centralwidget)
        self.signInForum_label.setGeometry(QtCore.QRect(40, 10, 191, 41))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        self.signInForum_label.setFont(font)
        self.signInForum_label.setObjectName("signInForum_label")
        SignInWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SignInWindow)
        self.statusbar.setObjectName("statusbar")
        SignInWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignInWindow)
        QtCore.QMetaObject.connectSlotsByName(SignInWindow)

        self.submit.pressed.connect(self.submitButton)
        
        self.conn = sqlite3.connect("data/database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,email TEXT,level INTEGER,password TEXT)")
        self.c.close()

    def retranslateUi(self, SignInWindow):
        _translate = QtCore.QCoreApplication.translate
        SignInWindow.setWindowTitle(_translate("SignInWindow", "Sign In"))
        self.password_label.setText(_translate("SignInWindow", "Password:"))
        self.email_label.setText(_translate("SignInWindow", "Email:"))
        self.level_label.setText(_translate("SignInWindow", "level:"))
        self.name_label.setText(_translate("SignInWindow", "Name:"))
        self.submit.setText(_translate("SignInWindow", "submit"))
        self.signInForum_label.setText(_translate("SignInWindow", "SIGN IN"))

        self.email_input.textChanged.connect(self.disableButton)
        self.name_input.textChanged.connect(self.disableButton)
        
        self.level_input.textChanged.connect(self.disableButton)
        self.password_input.textChanged.connect(self.disableButton)
            

    def submitButton(self):
        name = ""
        email = ""
        level = ""
        password = ""
        
        name = self.name_input.text()
        email = self.email_input.text()
        level = self.level_input.text()
        password = self.password_input.text()
    
        self.conn = sqlite3.connect("data/database.db")
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO students (name,email,level,password) VALUES (?,?,?,?)",(name,email,level,password))
        self.conn.commit()
        self.c.close()
        self.conn.close()
       
        self.popWindow()

    def disableButton(self):
        
        if len(self.name_input.text()) > 0 and len(self.email_input.text()) > 0 and len(self.level_input.text()) > 0 and len(self.password_input.text()) > 0:
            self.submit.setEnabled(True)

        else:
            self.submit.setEnabled(False)
