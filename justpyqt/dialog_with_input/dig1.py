from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLineEdit,QInputDialog,QHBoxLayout)
import sys

class FD(QWidget):
    def __init__(self):
        super().__init__()
        self.mysf()

    def mysf(self):
        hbox = QHBoxLayout()
        self.btn = QPushButton('ClickMe',self)
        self.btn.clicked.connect(self.sd)
        hbox.addWidget(self.btn)
        hbox.addStretch(1)

        self.le = QLineEdit(self)
        hbox.addWidget(self.le)

        self.setLayout(hbox)

        self.setWindowTitle("InputDialog")
        self.setGeometry(300,300,290,150)
        self.show()
    def sd(self):
        text , ok = QInputDialog.getText(self,'InputDialog','EnterYourName = ')
        if ok:
            self.le.setText(str(text))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    F = FD()
    sys.exit(app.exec_())