from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
from PyQt6.QtCore import QT_VERSION_STR
from PyQt6.QtCore import PYQT_VERSION_STR

print(QT_VERSION_STR)
print(PYQT_VERSION_STR)
print()
now = QDate.currentDate()
print(now.toString(Qt.DateFormat.ISODate))
print(now.toString())
print(now.toString(Qt.DateFormat.RFC2822Date))
nowdatetime = QDateTime.currentDateTime()
print (nowdatetime.toString())
nowtime = QTime.currentTime()
print (nowtime.toString())
