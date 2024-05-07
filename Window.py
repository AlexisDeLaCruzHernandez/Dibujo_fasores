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
        self.setFixedSize(500, 720)

        layout_h1 = QHBoxLayout()
        layout_h2 = QHBoxLayout()
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()
        layout_v3 = QVBoxLayout()
        layout_v4 = QVBoxLayout()

        self.module_label = Label("Módulo: ")
        layout_v1.addWidget(self.module_label)
        layout_v1.addSpacing(15)
        self.module = LineEdit("Módulo", 13)
        layout_v1.addWidget(self.module)
        layout_v1.addSpacing(15)

        self.angle_label = Label("Ángulo: ")
        layout_v2.addWidget(self.angle_label)
        layout_v2.addSpacing(15)
        self.angle = LineEdit("Ángulo", 13)
        layout_v2.addWidget(self.angle)
        layout_v2.addSpacing(15)

        self.label_label = Label("Etiqueta: ")
        layout_v3.addWidget(self.label_label)
        layout_v3.addSpacing(15)
        self.label = LineEdit("Etiqueta", 4)
        layout_v3.addWidget(self.label)
        layout_v3.addSpacing(15)

        self.actions_label = Label("Acciones: ")
        layout_h2.addWidget(self.actions_label)
        layout_h2.addSpacing(15)
        self.charge = Button("Cargar")
        self.charge.clicked.connect(lambda: self.graphic.plot_vector(self.module.text(),
                                                                     self.angle.text(),
                                                                     "a"+self.label.text()))
        layout_h2.addWidget(self.charge)
        layout_h2.addSpacing(15)
        self.delete = Button("Borrar")
        self.delete.clicked.connect(lambda: self.graphic.delete_plot())
        layout_h2.addWidget(self.delete)
        layout_h2.setContentsMargins(10, 0, 10, 0)

        self.graphic = Graphic(width=5, height=5, dpi=100)
        toolbar = ToolBar(self.graphic, self)

        layout_h1.addLayout(layout_v1)
        layout_h1.addSpacing(15)
        layout_h1.addLayout(layout_v2)
        layout_h1.addSpacing(15)
        layout_h1.addLayout(layout_v3)
        layout_h1.setContentsMargins(10, 0, 10, 0)

        layout_v4.addLayout(layout_h1)
        layout_v4.addSpacing(15)
        layout_v4.addLayout(layout_h2)
        layout_v4.addSpacing(15)
        layout_v4.addWidget(toolbar)
        layout_v4.addWidget(self.graphic)

        frame = QFrame()
        frame.setLayout(layout_v4)

        self.setCentralWidget(frame)
