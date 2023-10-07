class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		# ~ Set the default value for our variable.
		self.button_is_checked = True
		self.setWindowTitle("My App")
		button = QPushButton("Press Me!")
		button.setCheckable(True)
		button.clicked.connect(self.the_button_was_toggled)
		# ~ Use the default value to set the initial state of the widget.
		button.setChecked(self.button_is_checked)
		# Set the central widget of the Window.
		self.setCentralWidget(button)
	def the_button_was_toggled(self, checked):
		# ~ When the widget state changes, update the variable to match.
		self.button_is_checked = checked
		print(self.button_is_checked)
