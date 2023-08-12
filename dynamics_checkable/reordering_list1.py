import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton

class ReorderableListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reorderable List Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        reorder_button = QPushButton("Reorder Items")
        reorder_button.clicked.connect(self.reorder_items)
        layout.addWidget(reorder_button)

        update_button = QPushButton("Update List")
        update_button.clicked.connect(self.update_list)
        layout.addWidget(update_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        self.items = ["Item 1", "Item 2", "Item 3", "Item 4"]
        self.new_items = []  # Initialize as an empty list

        self.populate_list()

    def populate_list(self):
        self.list_widget.clear()
        self.list_widget.addItems(self.items)
        self.list_widget.setDragDropMode(QListWidget.InternalMove)

    def reorder_items(self):
        ordered_items = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
        print("Ordered Items:", ordered_items)
        self.items = ordered_items

    def update_list(self):
        self.items.extend(self.new_items)
        self.new_items = []  # Clear the new_items list
        self.populate_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReorderableListApp()
    window.show()
    sys.exit(app.exec_())
