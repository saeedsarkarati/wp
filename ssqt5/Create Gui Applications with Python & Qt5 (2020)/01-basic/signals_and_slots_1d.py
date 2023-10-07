class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.button_is_checked = True
		self.setWindowTitle("My App")
		
		# ~ We need to keep a reference to the button on self 
		# ~ so we can access it in our slot.		
		self.button = QPushButton("Press Me!")
		self.button.setCheckable(True)
		
		# ~ The released signal fires when the button is released, 
		# ~ but does not send the check state.
		self.button.released.connect(self.the_button_was_released)
		self.button.setChecked(self.button_is_checked)
		# Set the central widget of the Window.
		self.setCentralWidget(self.button)
	def the_button_was_released(self):
		# ~ .isChecked() returns the check state of the button.
		self.button_is_checked = self.button.isChecked()
		print(self.button_is_checked)
