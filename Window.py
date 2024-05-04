from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QFrame
from Config_widgets import Button, Label, LineEdit, Graphic, ToolBar
from PyQt6.QtGui import QIcon


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

        self.label1 = Label("Módulo: ")
        layout_v1.addWidget(self.label1)
        layout_v1.addSpacing(15)
        self.lineedit1 = LineEdit("Módulo")
        layout_v1.addWidget(self.lineedit1)

        self.label2 = Label("Ángulo: ")
        layout_v2.addWidget(self.label2)
        layout_v2.addSpacing(15)
        self.lineedit2 = LineEdit("Ángulo")
        layout_v2.addWidget(self.lineedit2)

        self.button3 = Button("Cargar")
        layout_v3.addWidget(self.button3)
        layout_v3.addSpacing(15)
        self.lineedit3 = LineEdit("Etiqueta")
        layout_v3.addWidget(self.lineedit3)

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
