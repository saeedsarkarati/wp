import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(400, 300)  # <1>
        self.canvas.fill(Qt.GlobalColor.white)  # <2>
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # tag::draw_something[]
    def draw_something(self):
        painter = QtGui.QPainter(self.canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRects(
            QtCore.QRect(50, 50, 100, 100),
            QtCore.QRect(60, 60, 150, 100),
            QtCore.QRect(70, 70, 100, 150),
            QtCore.QRect(80, 80, 150, 100),
            QtCore.QRect(90, 90, 100, 150),
        )
        painter.end()
        self.label.setPixmap(self.canvas)
    # end::draw_something[]


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
