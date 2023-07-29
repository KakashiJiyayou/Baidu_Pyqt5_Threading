import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QInputDialog, QLineEdit, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore
import PyQt5
from PyQt5 import QtGui

class MainWindow ( QMainWindow ):

    def __init__(self):
        super(MainWindow, self).__init__( )

        resource_path = 'Logo.ico'  # grabbed using preceding code
        pixmap = QtGui.QPixmap(resource_path)
        icon = QtGui.QIcon("Logo.ico")

        dlgi = QInputDialog()
        dlgi.setWindowIcon(icon)
        text, ok = dlgi.getText(self, 'InputDialog', 'EnterYourName = ')

        if ok:
            print( "PRint from input are", text )
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow()
    app.exec_()