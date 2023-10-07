from PyQt6.QtCore import QDateTime, Qt
now = QDateTime.currentDateTime()
print ('Local datetime: ', now.toString(Qt.DateFormat.ISODate))
print ('Universal datetime: ', now.toUTC().toString(Qt.DateFormat.ISODate))
print (f'The offset from UTC is: {now.offsetFromUtc()} seconds')
print (f'{1223232000:<20d} {2:^4}')
l = [1,2,3,4,5,6]
print (*l)
