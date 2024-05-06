from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

color_principal = "#FC93AD"


# Modified button
class Button(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(120, 35)
        self.setStyleSheet(
            "Button {"
            "font: bold 15px ;;"
            "border-radius: 13px ;;"
            "border: 2px solid" + color_principal + ";;"
            "padding: 1px 1px ;;"
            "color:" + color_principal + ";;"
            "background-color: #1C1C1C }"

            "Button:hover {"
            "background-color: #424242 }"

            "Button:pressed {"
            "border: 5px solid" + color_principal + "}"
        )


# Modified label
class Label(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(120, 35)
        self.setStyleSheet(
            "Label {"
            "font: bold 15px ;;"
            "border-bottom: 2px solid" + color_principal + ";;"
            "padding: 1px 1px ;;"
            "color:" + color_principal + ";;"
            "background-color: #1C1C1C }"
        )


# Modified line edit
class LineEdit(QLineEdit):
    def __init__(self, text):
        super().__init__()
        self.setPlaceholderText(text)
        self.setMaxLength(13)
        self.setFixedSize(120, 35)
        self.setStyleSheet(
            "LineEdit{"
            "border: 2px solid" + color_principal + ";;"
            "font: 15px ;;"
            "border-radius: 5px ;;"
            "padding: 1px 1px ;;"
            "color:" + color_principal + ";;"
            "background-color: #1C1C1C }"
        )


# Modified canvas
class Graphic(FigureCanvasQTAgg):
    def __init__(self, width=4, height=3, dpi=100):
        self.fig, self.ax1 = plt.subplots(1, 1, facecolor=color_principal, layout='constrained',
                                          figsize=(width, height), dpi=dpi)
        self.ax1.set_xticks([])
        self.ax1.set_yticks([])
        self.ax1.set_facecolor("#1C1C1C")
        for axis in ['top', 'bottom', 'left', 'right']:
            self.ax1.spines[axis].set_linewidth(0)
        super().__init__(self.fig)


# Modified toolbar
class ToolBar(NavigationToolbar):
    def __init__(self, graphic, parent=None):
        super().__init__(graphic, parent)
        unwanted_buttons = ["Customize", "Subplots", "Forward", "Back"]
        icons_buttons = {
            "Home": QIcon("Images/Home.png"),
            "Pan": QIcon("Images/Move.png"),
            "Zoom": QIcon("Images/Zoom_to_rect.png"),
            "Save": QIcon("Images/Filesave.png"),
        }

        for x in graphic.toolbar.actions():
            if x.text() in unwanted_buttons:
                self.removeAction(x)
            if x.text() in icons_buttons:
                x.setIcon(icons_buttons.get(x.text(), QIcon()))
        self.setStyleSheet(
            "color:" + color_principal + ";;"
            "background-color:" + "#1C1C1C" + ";;"
            "font: 15px ;;"
            "border-radius: 13px ;;"
            "min-height: 30px"
        )
