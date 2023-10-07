from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functools import partial

app = QApplication([])
window = QWidget()
# ~ window.setFixedSize(QSize(400, 300))
window.setGeometry(190,100,1000,600)
window.setWindowTitle("My App")
b = []
nb = 3
def aa(i):
	print (i.text())
	# ~ print (b[i].text())
for i in range (nb):
	b.append (QLabel( parent = window))
	b[i].setText (str(i+10) )
	b[i].setGeometry(100 + i * 50,100,40,40)
	b[i].linkActivated.connect (partial(aa, b[i]))
	# ~ b[i].clicked.connect (partial(aa, i))
window.show()
app.exec()
