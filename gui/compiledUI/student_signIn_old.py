from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_SignInWindow(object):
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
        self.email_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 3, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 0, 1, 1, 1)
        self.level_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.level_label.setFont(font)
        self.level_label.setObjectName("level_label")
        self.gridLayout.addWidget(self.level_label, 1, 0, 1, 1)
        self.level_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.level_input.setObjectName("level_input")
        self.gridLayout.addWidget(self.level_input, 1, 1, 1, 1)
        self.email_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_input.setObjectName("email_input")
        self.gridLayout.addWidget(self.email_input, 2, 1, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 3, 1, 1, 1)
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
        
        

    def retranslateUi(self, SignInWindow):
        _translate = QtCore.QCoreApplication.translate
        SignInWindow.setWindowTitle(_translate("SignInWindow", "Sign In"))
        self.email_label.setText(_translate("SignInWindow", "Email:"))
        self.password_label.setText(_translate("SignInWindow", "Password:"))
        self.name_label.setText(_translate("SignInWindow", "Name:"))
        self.level_label.setText(_translate("SignInWindow", "level:"))
        self.signInForum_label.setText(_translate("SignInWindow", "SIGN IN"))

    def submitButton(self):
        form_dict = {"username":name_input, "email": email_input, "level" : level_input, "password": password_input}

        with open("data/student_account.json","a+") as file:
            json.dump(form_dict,file,sort_keys = True, indent = 3)