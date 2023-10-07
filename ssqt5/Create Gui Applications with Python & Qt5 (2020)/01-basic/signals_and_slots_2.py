from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton # ①
from PyQt5.QtCore import Qt
import sys
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__() # ②
		self.setWindowTitle("My App")
		self.button = QPushButton("Press Me!") # ①
		self.button.clicked.connect(self.the_button_was_clicked)
		# Set the central widget of the Window.
		self.setCentralWidget(self.button)
	def the_button_was_clicked(self):
		self.button.setText("You already clicked me.") # ②
		self.button.setEnabled(False) # ③
		# Also change the window title.
		self.setWindowTitle("My Oneshot App")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
'''
① We need to be able to access the button in our the_button_was_clicked
method, so we keep a reference to it on self.
② You can change the text of a button by passing a str to .setText().
③ To disable a button call .setEnabled() with False. '''
