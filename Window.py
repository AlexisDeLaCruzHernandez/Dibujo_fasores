from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QFrame
from Config_widgets import Button, Label, LineEdit, Graphic, ToolBar
from PyQt6.QtGui import QIcon


# Modified main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1C1C1C")
        self.setWindowTitle("Graficador de fasores")
        self.setWindowIcon(QIcon("Images/Icon.png"))
        self.setFixedSize(500, 600)

        layout_h = QHBoxLayout()
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()
        layout_v3 = QVBoxLayout()
        layout_v4 = QVBoxLayout()

        self.module_label = Label("Módulo: ")
        layout_v1.addWidget(self.module_label)
        layout_v1.addSpacing(15)
        self.module = LineEdit("Módulo")
        layout_v1.addWidget(self.module)

        self.angle_label = Label("Ángulo: ")
        layout_v2.addWidget(self.angle_label)
        layout_v2.addSpacing(15)
        self.angle = LineEdit("Ángulo")
        layout_v2.addWidget(self.angle)

        self.charge = Button("Cargar")
        self.charge.clicked.connect(lambda: self.graphic.plot_vector(self.module.text(),
                                                                     self.angle.text(),
                                                                     self.label.text()))
        layout_v3.addWidget(self.charge)
        layout_v3.addSpacing(15)
        self.label = LineEdit("Etiqueta")
        layout_v3.addWidget(self.label)

        self.graphic = Graphic(width=5, height=4, dpi=100)
        toolbar = ToolBar(self.graphic, self)

        layout_h.addLayout(layout_v1)
        layout_h.addSpacing(15)
        layout_h.addLayout(layout_v2)
        layout_h.addSpacing(15)
        layout_h.addLayout(layout_v3)
        layout_h.setContentsMargins(10, 0, 10, 0)

        layout_v4.addLayout(layout_h)
        layout_v4.addWidget(toolbar)
        layout_v4.addWidget(self.graphic)

        frame = QFrame()
        frame.setLayout(layout_v4)

        self.setCentralWidget(frame)
