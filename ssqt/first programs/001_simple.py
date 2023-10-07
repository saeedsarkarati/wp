import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMdiSubWindow, QMainWindow

def main():

	app = QApplication(sys.argv)

	# ~ w = QWidget()
	# ~ w = QMdiSubWindow()
	w = QMainWindow()
	w.resize(250, 100)
	w.move(400, 100)
	# ~ w.setGeometry(100, 300, 400, 200)

	width = w.frameGeometry().width()
	print (width)
	w.setWindowTitle(f'Simple{width}'+ 'برنامه')
	w.move(400, 400)
	w.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
