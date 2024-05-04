from PyQt6.QtWidgets import QApplication
from Window import MainWindow

App = QApplication([])

Window = MainWindow()
Window.show()

App.exec()
