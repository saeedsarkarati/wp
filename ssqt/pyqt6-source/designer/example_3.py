import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtUiTools import QUiLoader

loader = QUiLoader()


class MainUI(QtCore.QObject):  # Not a widget.
    def __init__(self):
        super().__init__()
        self.ui = loader.load("mainwindow.ui", None)
        self.ui.setWindowTitle("MainWindow Title")
        self.ui.show()


app = QtWidgets.QApplication(sys.argv)
ui = MainUI()
app.exec()
