a = 10
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()
print(time.toString(Qt.DateFormat.ISODate))


# ~ --------

now = QDateTime.currentDateTime()

print('Local datetime: ', now.toString(Qt.DateFormat.ISODate))
print('Universal datetime: ', now.toUTC().toString(Qt.DateFormat.ISODate))

print(f'The offset from UTC is: {now.offsetFromUtc()} seconds')
# ~ -----------
now = QDate.currentDate()

d = QDate(1945, 5, 7)

print(f'Days in month: {d.daysInMonth()}')
print(f'Days in year: {d.daysInYear()}')
# ~ ------------
now = QDate.currentDate()
y = now.year()

print(f'today is {now.toString(Qt.DateFormat.ISODate)}')

xmas1 = QDate(y-1, 12, 25)
xmas2 = QDate(y, 12, 25)

dayspassed = xmas1.daysTo(now)
print(f'{dayspassed} days have passed since last XMas')

nofdays = now.daysTo(xmas2)
print(f'There are {nofdays} days until next XMas')
# ~ ------------------
now = QDateTime.currentDateTime()

print(f'Today: {now.toString(Qt.DateFormat.ISODate)}')
print(f'Adding 12 days: {now.addDays(12).toString(Qt.DateFormat.ISODate)}')
print(f'Subtracting 22 days: {now.addDays(-22).toString(Qt.DateFormat.ISODate)}')

print(f'Adding 50 seconds: {now.addSecs(50).toString(Qt.DateFormat.ISODate)}')
print(f'Adding 3 months: {now.addMonths(3).toString(Qt.DateFormat.ISODate)}')
print(f'Adding 12 years: {now.addYears(12).toString(Qt.DateFormat.ISODate)}')
# ~ -------------
now = QDateTime.currentDateTime()

print(f'Time zone: {now.timeZoneAbbreviation()}')

if now.isDaylightTime():
    print('The current date falls into DST time')
else:
    print('The current date does not fall into DST time')
# ~ -------------
now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch() 
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.DateFormat.ISODate))
