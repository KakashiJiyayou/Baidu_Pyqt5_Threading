import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QInputDialog, QLineEdit, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore
import PyQt5
from PyQt5 import QtGui

class MainWindow ( QMainWindow ):

    def __init__(self):
        super().__init__( )

        dlgi = QInputDialog()
        text, ok = dlgi.getText(self, 'InputDialog', 'EnterYourName = ')

        if ok:
            print( "PRint from input are", text )
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
    print ("process doen")