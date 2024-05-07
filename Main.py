from PyQt6.QtWidgets import QApplication
from Window import MainWindow


# Create app
App = QApplication([])

# Create and show main window
Window = MainWindow()
Window.show()

# App execution
App.exec()
