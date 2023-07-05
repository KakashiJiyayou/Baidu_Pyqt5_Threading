


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtOpenGL import *

image_path_str='image.jpg'

class View(QGraphicsView):
    # photo_clicked = QtCore.Signal(QtCore.QPoint)

    def __init__(self, parent):
        super(View, self).__init__()
        self.scene = QtWidgets.QGraphicsScene(self)
        self.photo = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.photo)
        self.pixmap = QtGui.QPixmap(image_path_str)
        self.photo.setPixmap(self.pixmap)
        self.setScene(self.scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.view = View(self)

        self.layout_contain_P1_P2 = QtWidgets.QGridLayout()
        self.checkbox_P1= QtWidgets.QCheckBox("P1",self)
        self.line_edit_P1_x = QtWidgets.QLineEdit(self)
        self.line_edit_P1_x.setReadOnly(True)
        self.line_edit_P1_y = QtWidgets.QLineEdit(self)
        self.line_edit_P1_y.setReadOnly(True)

        self.layout_contain_P1_P2.addWidget(self.checkbox_P1, 0, 0, Qt.AlignLeft)

        self.grid_layout_P1_x_y = QtWidgets.QGridLayout()
        self.grid_layout_P1_x_y.addWidget(self.line_edit_P1_x, 1, 0, Qt.AlignLeft)
        self.grid_layout_P1_x_y.addWidget(self.line_edit_P1_y, 2, 0, Qt.AlignLeft)

        self.layout_contain_P1_P2.addLayout(self.grid_layout_P1_x_y, 0, 1, 1, 1)
        self.checkbox_P2 = QtWidgets.QCheckBox("P2",self)
        self.line_edit_P2_x = QtWidgets.QLineEdit(self)
        self.line_edit_P2_x.setReadOnly(True)
        self.line_edit_P2_y = QtWidgets.QLineEdit(self)
        self.line_edit_P2_y.setReadOnly(True)

        self.layout_contain_P1_P2.addWidget(self.checkbox_P2, 1, 0, Qt.AlignLeft)
        self.grid_layout_P2_x_y = QtWidgets.QGridLayout()

        self.grid_layout_P2_x_y.addWidget(self.line_edit_P2_x, 0, 0, Qt.AlignLeft)
        self.grid_layout_P2_x_y.addWidget(self.line_edit_P2_y, 1, 0, Qt.AlignLeft)

        self.layout_contain_P1_P2.addLayout(self.grid_layout_P2_x_y, 1, 1, Qt.AlignLeft)

        self.combo_box1 = QtWidgets.QComboBox(self)
        self.combo_box1.addItem("measurements set 1")
        self.combo_box1.addItem("measurements set 1")

        self.combo_box2 = QtWidgets.QComboBox(self)
        self.combo_box2.addItem("P1-P2")
        self.combo_box2.addItem("P3-P4")

        self.vertical1= QtWidgets.QVBoxLayout()

        self.vertical1.addWidget(self.combo_box1)
        self.vertical1.addWidget(self.combo_box2)
        self.vertical1.addLayout(self.layout_contain_P1_P2)

        self.vertical2= QtWidgets.QVBoxLayout()
        self.vertical2.addWidget(self.view)

        self.horizontal= QtWidgets.QHBoxLayout()
        self.horizontal.addLayout(self.vertical1)
        self.horizontal.addLayout(self.vertical2)

        self.setLayout(self.horizontal)
        self.setWindowTitle("Image viewer")
        self.setGeometry(200, 200, 1000, 800)

app = QApplication.instance()
if app is None:
        app = QApplication([])
w = Window()
w.show()
w.raise_()
QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
app.exec_()