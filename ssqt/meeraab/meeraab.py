from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from functools import partial

app = QApplication([])
window = QMainWindow()
window.setFixedSize(QSize(400, 300))
window.setGeometry(190,100,400,400)
window.setWindowTitle("My App")
b = []
nb = 3
def aa(i):
	print (i.text())
for i in range (nb):
	b.append (QPushButton( parent = window))
	b[i].setText (str(i+10) )
	b[i].setGeometry(100 + i * 50,100,40,40)
	b[i].clicked.connect (partial(aa,b[i]))
window.show()
app.exec()
