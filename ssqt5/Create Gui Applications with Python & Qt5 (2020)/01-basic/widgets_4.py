import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")
		self.widget = QComboBox(parent = self)
		self.setGeometry(100, 100, 600, 600)
		self.widget.setGeometry(80, 130, 86, 25)

		self.widget.addItems(["One", "Two", "Three"])
		self.widget.currentIndexChanged.connect(self.index_changed)
		self.widget.currentTextChanged.connect(self.text_changed)
	def index_changed(self, i):
		print("i",i)# i is an int
		if i == 2: 
			self.widget.setGeometry(180, 130, 86, 25)
		if i == 1: 
			self.widget.setGeometry(80, 230, 86, 25)
		if i == 0: 
			self.widget.setGeometry(180, 130, 186, 25)
		
	def text_changed(self, s):
		print("s",s)# s is a str
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
