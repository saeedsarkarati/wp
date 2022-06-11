import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")
		button = QPushButton("class")
		self.setMaximumSize(QSize(400, 300))
		# Set the central widget of the Window.
		self.setCentralWidget(button)
app = QApplication(sys.argv)
window = MainWindow()
window.setMaximumSize(QSize(400, 400))
window.setWindowTitle("class 2")
window.show()
ww = MainWindow()
ww.show()
w = QMainWindow()
w.setWindowTitle("sssss")
w.setMinimumSize(QSize(400, 300))
button = QPushButton("ssss")
w.setCentralWidget(button)
w.show()
app.exec()
