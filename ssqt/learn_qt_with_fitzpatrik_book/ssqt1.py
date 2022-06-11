from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QMainWindow
# ~ import sys
# ~ app = QApplication(sys.argv)
app = QApplication([])
w = []
w.append ( QPushButton("Push Me"))
w.append (QWidget())
w.append (QMainWindow() )
for i in w:
	i.show()
app.exec()
