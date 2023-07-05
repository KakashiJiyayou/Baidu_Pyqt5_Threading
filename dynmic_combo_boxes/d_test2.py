from PySide2.QtWidgets import QWidget, QApplication, QGraphicsView, QGridLayout, QComboBox, \
     QGraphicsScene, QGraphicsPixmapItem, QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Signal, QPoint, Qt
from PySide2.QtGui import QPixmap, QStandardItemModel, QStandardItem, QCursor

image_path_str='image.jpg'

class View(QGraphicsView):
    photo_clicked = Signal(QPoint)

    def __init__(self, parent):
        super(View, self).__init__()
        self.scene = QGraphicsScene(self)
        self.photo = QGraphicsPixmapItem()
        self.scene.addItem(self.photo)
        self.pixmap = QPixmap(image_path_str)
        self.photo.setPixmap(self.pixmap)
        self.setScene(self.scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.view = View(self)

        self.layout_contain_P1_P2 = QGridLayout()
        self.checkbox_P1= QCheckBox("P1",self)
        self.line_edit_P1_x = QLineEdit(self)
        self.line_edit_P1_x.setReadOnly(True)
        self.line_edit_P1_y = QLineEdit(self)
        self.line_edit_P1_y.setReadOnly(True)

        self.layout_contain_P1_P2.addWidget(self.checkbox_P1, 0, 0, Qt.AlignLeft)

        self.grid_layout_P1_x_y = QGridLayout()
        self.grid_layout_P1_x_y.addWidget(self.line_edit_P1_x, 1, 0, Qt.AlignLeft)
        self.grid_layout_P1_x_y.addWidget(self.line_edit_P1_y, 2, 0, Qt.AlignLeft)

        self.layout_contain_P1_P2.addLayout(self.grid_layout_P1_x_y, 0, 1, 1, 1)
        self.checkbox_P2 = QCheckBox("P2",self)
        self.line_edit_P2_x = QLineEdit(self)
        self.line_edit_P2_x.setReadOnly(True)
        self.line_edit_P2_y = QLineEdit(self)
        self.line_edit_P2_y.setReadOnly(True)

        self.layout_contain_P1_P2.addWidget(self.checkbox_P2, 1, 0, Qt.AlignLeft)
        self.grid_layout_P2_x_y = QGridLayout()

        self.grid_layout_P2_x_y.addWidget(self.line_edit_P2_x, 0, 0, Qt.AlignLeft)
        self.grid_layout_P2_x_y.addWidget(self.line_edit_P2_y, 1, 0, Qt.AlignLeft)

        self.layout_contain_P1_P2.addLayout(self.grid_layout_P2_x_y, 1, 1, Qt.AlignLeft)

        self.vertical1= QVBoxLayout()

        self.model = create_model(d)
        ix = self.model.index(0, 0)
        self.combos = []
        while self.model.hasChildren(ix):
            combo = QComboBox()
            combo.setModel(self.model)
            self.vertical1.addWidget(combo)
            combo.setRootModelIndex(ix)
            combo.setCurrentIndex(0)
            ix = ix.child(0, 0)
            combo.currentIndexChanged.connect(self.on_currentIndexChanged)
            self.combos.append(combo)

        self.vertical1.addLayout(self.layout_contain_P1_P2)

        self.vertical2= QVBoxLayout()
        self.vertical2.addWidget(self.view)

        self.horizontal= QHBoxLayout()
        self.horizontal.addLayout(self.vertical1)
        self.horizontal.addLayout(self.vertical2)

        self.setLayout(self.horizontal)
        self.setWindowTitle("Image viewer")
        self.setGeometry(200, 200, 1000, 800)

    def next_combo(self, combo):
        ix = self.combos.index(combo)
        if ix != len(self.combos)-1:
            return self.combos[ix+1]

    def on_currentIndexChanged(self, index):
        combo = self.sender()
        combo_child = self.next_combo(combo)
        if combo_child:
            p_ix = combo.rootModelIndex()
            ix = p_ix.child(index, 0)
            combo_child.setRootModelIndex(ix)
            combo_child.setCurrentIndex(0)

def load_childrens(values, parent):
    for value in values:
        name = value["name"]
        dependencies = value["dependencies"]
        item = QStandardItem(name)
        parent.appendRow(item)
        load_childrens(dependencies, item)

def create_model(info):
    model = QStandardItemModel()
    root = QStandardItem("root")
    model.appendRow(root)
    load_childrens(info, root)
    return model


d = [{
        'name': 'measurements set 1',
        'dependencies': [
            {
                'name': 'P1-P2',
                'dependencies': []
            },
            {
                'name': 'P3-P4',
                'dependencies': []
            }
        ],
    },
    {
        'name': 'measurements set 2',
        'dependencies': [
            {
                'name': 'P5-P6',
                'dependencies': []
            },
            {
                'name': 'P7-P8',
                'dependencies': []
            }
        ],
    }]

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.setOverrideCursor(QCursor(Qt.CrossCursor))
    sys.exit(app.exec_())