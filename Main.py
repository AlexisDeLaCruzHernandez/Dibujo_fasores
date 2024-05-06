from PyQt6.QtWidgets import QApplication
from numpy import cos, sin, radians
from Window import MainWindow

axis = []


def plot_vector():
    try:
        module = float(Window.module.text().replace(",", "."))
        angle = radians(float(Window.angle.text().replace(",", ".")))
    except ValueError:
        print("Mostrar ventana de error")
        return
    x_value = module * cos(angle)
    axis.append(x_value)
    y_value = module * sin(angle)
    axis.append(y_value)
    Window.graphic.ax1.quiver(0, 0, x_value, y_value, scale_units="xy", angles="xy", color="red", scale=1)
    Window.graphic.ax1.axis([-max(axis)-10, max(axis)+10, -max(axis)-10, max(axis)+10])
    Window.graphic.draw()


# Create app
App = QApplication([])

# Create and show main window
Window = MainWindow()
Window.show()

# Connect button to function
Window.charge.clicked.connect(plot_vector)

App.exec()
