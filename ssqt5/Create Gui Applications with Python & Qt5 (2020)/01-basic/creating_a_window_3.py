from PyQt5.QtWidgets import QApplication, QMainWindow
app = QApplication([])
window = QMainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec_()
