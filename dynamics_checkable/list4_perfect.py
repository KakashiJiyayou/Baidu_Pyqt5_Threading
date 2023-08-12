import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QPushButton, QMessageBox

class DynamicChecklistApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()



    def initUI(self):
        # Set up main window properties
        self.setWindowTitle('Dynamic Check List')

        # Create a central widget and set it as central
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        # Set up layout for the central widget
        layout = QVBoxLayout(self._central_widget)

        # Create a layout for the list of checkboxes
        self._checkbox_layout = QVBoxLayout()
        layout.addLayout(self._checkbox_layout)

        # Create a layout for the buttons
        self._button_layout = QVBoxLayout()
        layout.addLayout(self._button_layout)

        # Create a button to update the list
        self._update_button = QPushButton('Update List')
        self._update_button.clicked.connect(self.update_list)
        self._button_layout.addWidget(self._update_button)

        # Create a button to show selected items
        self._show_selected_button = QPushButton('Show Selected Items')
        self._show_selected_button.clicked.connect(self.show_selected_items)
        self._button_layout.addWidget(self._show_selected_button)

        # Initialize an empty list of checkboxes
        self._checkboxes = []

        # Initialize new_item_list as an empty list
        self.new_item_list_generate_doc = []

    def update_list(self):
        # Clear existing checkboxes
        for checkbox in self._checkboxes:
            checkbox.setParent(None)
            checkbox.deleteLater()
        self._checkboxes.clear()

        # Create checkboxes for new items
        for i, item in enumerate(self.new_item_list_generate_doc):
            checkbox = QCheckBox(item)
            self._checkbox_layout.addWidget(checkbox)
            self._checkboxes.append(checkbox)

    def show_selected_items(self):
        selected_items = [checkbox.text() for checkbox in self._checkboxes if checkbox.isChecked()]
        selected_text = "\n".join(selected_items)

        if selected_text:
            print("Selected Items:")
            print(selected_text)
            QMessageBox.information(self, "Selected Items", selected_text)
        else:
            QMessageBox.information(self, "Selected Items", "No items selected.")

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DynamicChecklistApp()

    # Read data from "dir_list.json" or use a default list
    json_data = read_json_file('dir_list.json')
    window.new_item_list_generate_doc = json_data if json_data else ['Item 1', 'Item 2', 'Item 3']

    window.update_list()

    window.show()
    sys.exit(app.exec_())
