import sys
import json
from PyQt5.QtCore import Qt, QAbstractListModel, QModelIndex, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAbstractItemView, QListView, QPushButton, QMessageBox

class ReorderListModel(QAbstractListModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()]

    def rowCount(self, parent):
        return len(self._data)

    def supportedDropActions(self):
        return Qt.MoveAction

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild):
        if destinationChild != -1:
            self.beginMoveRows(sourceParent, sourceRow, sourceRow + count - 1, destinationParent, destinationChild)
            self._data.insert(destinationChild, self._data.pop(sourceRow))
            self.endMoveRows()
            return True
        return False

class ReorderListView(QListView):
    def __init__(self, data):
        super().__init__()
        self.setModel(ReorderListModel(data))
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

    def update_list(self, data):
        model = ReorderListModel(data)
        self.setModel(model)

class DynamicChecklistApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set up main window properties
        self.setWindowTitle('Dynamic Check List')
        self.setGeometry(100, 100, 400, 400)

        # Create a central widget and set it as central
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        # Set up layout for the central widget
        layout = QVBoxLayout(self._central_widget)

        # Load data from "dir_list.json"
        self._file_locations = self.read_json_file('dir_list.json')

        # Replace QListWidget with custom ReorderListView
        self._record_list_view = ReorderListView(self._file_locations)
        layout.addWidget(self._record_list_view)

        # Create a button to update the list
        self._update_button = QPushButton('Update List')
        self._update_button.clicked.connect(self.update_list)
        layout.addWidget(self._update_button)

       


    def update_list(self):
        # Update the list view by re-reading the JSON file
        self.file_locations = self.read_json_file('dir_list.json')
        self.check_list_view.update_list(self.file_locations)

    def read_json_file(self, file_path):
        try:
            with open(file_path) as f:
                data = json.load(f)
                return data
        except Exception as e:
            print("Error reading JSON:", e)
            return []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DynamicChecklistApp()
    window.show()
    sys.exit(app.exec_())
