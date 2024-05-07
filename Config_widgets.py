from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from numpy import cos, sin, radians

principal_color = "#FC93AD"


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
            "border: 2px solid" + principal_color + ";;"
            "padding: 1px 1px ;;"
            "color:" + principal_color + ";;"
            "background-color: #1C1C1C }"

            "Button:hover {"
            "background-color: #424242 }"

            "Button:pressed {"
            "border: 5px solid" + principal_color + "}"
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
            "border-bottom: 2px solid" + principal_color + ";;"
            "padding: 1px 1px ;;"
            "color:" + principal_color + ";;"
            "background-color: #1C1C1C }"
        )


# Modified line edit
class LineEdit(QLineEdit):
    def __init__(self, text, max_length):
        super().__init__()
        self.setPlaceholderText(text)
        self.setMaxLength(max_length)
        self.setFixedSize(120, 35)
        self.setStyleSheet(
            "LineEdit{"
            "border: 2px solid" + principal_color + ";;"
            "font: 15px ;;"
            "border-radius: 5px ;;"
            "padding: 1px 1px ;;"
            "color:" + principal_color + ";;"
            "background-color: #1C1C1C }"
        )


# Modified canvas
class Graphic(FigureCanvasQTAgg):
    def __init__(self, width=4, height=3, dpi=100):
        self.colors = {
            "Current": "#51CCFE",
            "Voltage": "#51FE6B",
            "Default": principal_color,
        }
        self.axis_limit = 0
        self.fig, self.ax1 = plt.subplots(1, 1, facecolor=principal_color, layout='constrained',
                                          figsize=(width, height), dpi=dpi)
        self.ax1.set_xticks([])
        self.ax1.set_yticks([])
        self.ax1.set_facecolor("#1C1C1C")
        for axis in ['top', 'bottom', 'left', 'right']:
            self.ax1.spines[axis].set_linewidth(0)
        super().__init__(self.fig)

    def plot_vector(self, module, angle, label):
        # Transform string in coordinates
        try:
            module = float(module.replace(",", "."))
            angle = radians(float(angle.replace(",", ".")))
        except ValueError:
            print("Mostrar ventana de error")
            return
        x_value = module * cos(angle)
        y_value = module * sin(angle)

        # Detect the type of the label and transform to LaTeX
        label = label[1:]
        color = self.colors.get("Default")
        if label:
            if label[0] == "I" or label == "i":
                color = self.colors.get("Current")
                label = "$" + label[0] + "_{" + label[1:] + "}$"
            elif label[0] == "V" or label[0] == "v":
                color = self.colors.get("Voltage")
                label = "$" + label[0] + "_{" + label[1:] + "}$"
            else:
                label = "$" + label + "$"

        # Setting the axis limit
        if abs(x_value) > self.axis_limit:
            self.axis_limit = abs(x_value)
        elif abs(y_value) > self.axis_limit:
            self.axis_limit = abs(y_value)
        margin = self.axis_limit * 0.25

        # Setting the place of the label
        move_text = [0, 0]
        if x_value > 0:
            move_text[0] = self.axis_limit * 0.02 + x_value
        elif x_value < 0:
            move_text[0] = -self.axis_limit * 0.12 + x_value
        if y_value > 0:
            move_text[1] = self.axis_limit * 0.02 + y_value
        elif y_value < 0:
            move_text[1] = -self.axis_limit * 0.06 + y_value

        # Ploting
        self.ax1.quiver(0, 0, x_value, y_value, scale_units="xy", angles="xy", color=color, scale=1)
        self.ax1.annotate(label, xy=(x_value, y_value), xytext=move_text, color=color)
        self.ax1.axis([-self.axis_limit - margin, self.axis_limit + margin,
                       -self.axis_limit - margin, self.axis_limit + margin])
        self.draw()

    def delete_plot(self):
        self.ax1.cla()
        self.ax1.set_xticks([])
        self.ax1.set_yticks([])
        self.draw()


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
            "color:" + principal_color + ";;"
            "background-color:" + "#1C1C1C" + ";;"
            "font: 15px ;;"
            "border-radius: 13px ;;"
            "min-height: 30px"
        )
