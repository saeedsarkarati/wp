

import sys
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
	
        self.initUI()
        # ~ self.move(500, 400)


    def initUI(self):

        self.resize(350, 250)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        # ~ print (cp)
		
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.move(500, 400)
		

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
