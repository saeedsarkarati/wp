import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from functools import partial

# Subclass QMainWindow to customize your application's main window
app = QApplication(sys.argv)
class SSWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(190,100,400,400)
		self.setWindowTitle("My App")
		b = []
		nb = 3
		for i in range (nb):
			b.append (QPushButton( parent = self))
			b[i].setText (str(i) )
			b[i].setGeometry(100 + i * 50,100,40,40)
			b[i].clicked.connect (self.aa)
	def aa(self,i):
		print (i)
	
window = SSWindow()
# ~ window.setFixedSize(QSize(400, 300))
window.show()
app.exec()
