import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QListWidgetItem, QCheckBox, \
    QPushButton, QMessageBox




class DynamicChecklistApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

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
        # Clear the existing items in the list widget
        self.check_list_widget.clear()

        # Load file locations from JSON
        file_locations = self.read_json_file('dir_list.json')

        # Populate the list widget with checkable items
        for location in file_locations:
            item = QListWidgetItem()
            checkbox = QCheckBox(location)
            item.setSizeHint(checkbox.sizeHint())
            self.check_list_widget.addItem(item)
            self.check_list_widget.setItemWidget(item, checkbox)

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
    window.show()
    sys.exit(app.exec_())
