from PyQt6.QtWidgets import QApplication
# from numpy import cos, sin, radians
from Window import MainWindow


# Create app
App = QApplication([])

# Create and show main window
Window = MainWindow()
Window.show()

# App execution
App.exec()
