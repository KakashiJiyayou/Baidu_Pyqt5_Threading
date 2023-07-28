import sys

from PyQt5 import QtCore, QtWidgets


class Terminal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.out = QtWidgets.QPlainTextEdit(readOnly=True)
        self.inBar = QtWidgets.QLineEdit()

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.out)
        layout.addWidget(self.inBar)

        self.process = QtCore.QProcess(self)
        self.process.setProgram(sys.executable)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.readyReadStandardError.connect(self.on_readyReadStandardError)
        self.inBar.editingFinished.connect(self.on_editingFinished)

    def runFile(self, url):
        self.process.setArguments([url])
        self.process.start()

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        out = self.process.readAllStandardOutput().data().decode()
        self.out.insertPlainText(out)

    @QtCore.pyqtSlot()
    def on_readyReadStandardError(self):
        err = self.process.readAllStandardError().data().decode()
        self.out.insertPlainText("\n" + err)

    @QtCore.pyqtSlot()
    def on_editingFinished(self):
        self.process.write(self.inBar.text().encode() + b"\n")
        self.inBar.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Terminal()
    window.runFile("bypy list")
    window.show()
    sys.exit(app.exec_())