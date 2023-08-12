
import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QListWidgetItem, QCheckBox, \
    QPushButton, QMessageBox


class DynamicChecklistApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Initialize new_item_list as an empty list
        self.new_item_list = []

    def initUI(self):
        # Set up main window properties
        self.setWindowTitle('Dynamic Check List')
        self.setGeometry(100, 100, 400, 400)

        # Create a central widget and set it as central
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up layout for the central widget
        layout = QVBoxLayout(self.central_widget)
        self.check_list_widget = QListWidget()  # List widget to display checkable items
        layout.addWidget(self.check_list_widget)

        # Create and connect a button to show selected items
        self.update_button = QPushButton('Show Selected Items')
        self.update_button.clicked.connect(self.show_selected_items)
        layout.addWidget(self.update_button)

        # Populate the list widget with items
        self.update_checklist()

    def read_json_file(self, file_path):
        try:
            with open(file_path) as f:
                data = json.load(f)
                return data
        except Exception as e:
            print("Error reading JSON:", e)
            return []

    def update_checklist(self):
        # Clear existing checkboxes
        for checkbox in self._checkboxes:
            checkbox.setParent(None)
            checkbox.deleteLater()
        self._checkboxes.clear()

        # Create checkboxes for new items
        for i, item in enumerate(self.new_item_list):
            checkbox = QCheckBox(item)
            self._checkbox_layout.addWidget(checkbox)
            self._checkboxes.append(checkbox)

    def show_selected_items(self):
        selected_items = []

        # Iterate through checklist to find selected items
        for index in range(self.check_list_widget.count()):
            item = self.check_list_widget.item(index)
            checkbox = self.check_list_widget.itemWidget(item)

            if checkbox.isChecked():
                selected_items.append(checkbox.text())

        if selected_items:
            selected_text = "\n".join(selected_items)
            print("Selected Items:")
            print(selected_text)
            print("Selected Items as list:", selected_items)  # Print as a list
            QMessageBox.information(self, "Selected Items", selected_text)
        else:
            QMessageBox.information(self, "Selected Items", "No items selected.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DynamicChecklistApp()

    # Read data from "dir_list.json" or use a default list
    json_data = window.read_json_file('dir_list.json')
    window.new_item_list = json_data if json_data else ['Item 1', 'Item 2', 'Item 3']

    window.update_list()

    window.show()
    sys.exit(app.exec_())