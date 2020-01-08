from PyQt5 import QtWidgets
from compiledUI.menu import *
import os
import sys

def cls():
    os.system('Cls ' if os.name =='nt' else 'clear')

def main(): 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    window = Ui_MenuWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()