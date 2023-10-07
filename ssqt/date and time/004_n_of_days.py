from PyQt6.QtCore import QDate
n = QDate.currentDate()
d = QDate(1945, 2, 17)
print(f'Days in month: {d.daysInMonth()}')
print(f'Days in year: {d.daysInYear()}')

print(f'Days in month: {n.daysInMonth()}')
print(f'Days in year: {n.daysInYear()}')
