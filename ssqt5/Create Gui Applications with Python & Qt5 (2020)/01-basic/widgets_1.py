import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")
		widget = QLabel("Hello")
		font = widget.font() # ①
		font.setPointSize(30)
		widget.setFont(font)
		widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		# ②
		self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
'''① We get the current font, using <widget>.font(), modify it and then apply it
back. This ensures the font face remains in keeping with the desktop
conventions.
② The alignment is specified by using a flag from the Qt. namespace '''
