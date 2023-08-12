import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QListWidgetItem, QCheckBox

class DynamicChecklistApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dynamic Check List')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        self.check_list_widget = QListWidget()
        layout.addWidget(self.check_list_widget)

        # Load data from "dir_list.json"
        with open('dir_list.json') as f:
            file_locations = json.load(f)

        # Populate list with checkable items
        for location in file_locations:
            item = QListWidgetItem(self.check_list_widget)
            checkbox = QCheckBox(location)
            item.setSizeHint(checkbox.sizeHint())
            self.check_list_widget.setItemWidget(item, checkbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DynamicChecklistApp()
    window.show()
    sys.exit(app.exec_())
