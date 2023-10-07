from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPainter, QFont
def token9(ws, FI):
	print(ws.cell(FI, 8).value)
	def drawtext(x, y, s, v = 0):
		if v == 0:
			ss = s
		else:
			ss = str(ws.cell(FI, v).value)
			if ss == 'None':
				ss = '.....'
			ss = s + ' ' +ss
		painter.drawText(x - 150, y, 450, 100, Qt.AlignRight, ss)

	w = 1000
	h = 1400
	line = {
		'0' : 150,	'1' : 200,	'2' : 250, 	'3' : 300, 	'4' : 350, 	'5' : 400,
		'6' : 450,	'7' : 500,	'8' : 550,	'9' : 600,	'10' : 650,	'11' : 700,
		'12' : 750,	'13' : 800,	'14' : 850,	'15' : 900,	'16' : 950,	'17' : 1000,
		'18' : 1050,'19' : 1100,'20' : 1150,'21' : 1200,'22' : 1250,
	}
	canvas = QPixmap(w, h)
	canvas.fill(QColor(255, 255, 255))
	painter = QPainter(canvas)
	font = QFont()
	font.setFamily("IRZar")
	font.setBold(True)
	font.setPointSize(22)
	painter.setFont(font)
	painter.drawText(250, line['0'], "فرم شماره ۹: صدور توکن شارژ (درخواست شارژ کنتور) ")
	font.setBold(False)
	font.setPointSize(14)
	painter.setFont(font)
	painter.drawText(150, line['1'], "شماره:......")
	painter.drawText(150, line['2'], "تاریخ:......")

	font.setBold(True)
	font.setUnderline(True)
	font.setPointSize(17)
	painter.setFont(font)
	drawtext(650, line['3'], "مشخصات چاه")
	drawtext(650, line['6'], "مشخصات متقاضی")
	drawtext(650, line['12'], "نحوه‌ی اختصاص سهم‌آب سالیانه")
	drawtext(650, line['17'], "مشخصات شارژ مورد نیاز:")

	font.setBold(False)
	font.setUnderline(False)
	font.setPointSize(16)
	painter.setFont(font)
	drawtext(650, line['4'], "شهرستان:", 1)
	drawtext(440, line['4'], "دشت:", 2)
	drawtext(240, line['4'], "امور آب تابعه:", 3)
	drawtext(650, line['5'], "نام منبع:", 4)
	drawtext(440, line['5'], "شماره کلاسه پرونده:", 5)
	drawtext(150, line['5'], "نوع مصرف:", 6)
	drawtext(650, line['7'], "مالک "+chr(9634))
	drawtext(480, line['7'], "نماینده مالک یا تعدادی از مالکین " +chr(9634))
	drawtext(150, line['7'], "نماینده شخص حقوقی " +chr(9634))
	drawtext(650, line['8'], "نام:", 7)
	drawtext(550, line['8'], "نام خانوداگی:", 8)
	drawtext(350, line['8'], "نام پدر:", 9)
	drawtext(150, line['8'], "شماره شناسنامه:", 10)
	drawtext(650, line['9'], "شماره ملی:", 11)
	drawtext(350, line['9'], "تلفن همراه:", 12)
	drawtext(150, line['9'], "کد پستی", 13)
	drawtext(650, line['10'], "آدرس:", 14)
	drawtext(650, line['11'], "شماره وکالت‌نامه:", 15)
	drawtext(350, line['11'], "تاریخ ثبت وکالتنامه:", 16)
	drawtext(150, line['11'], "شماره دفترخانه:", 17)
	drawtext(650, line['13'], "اختصاص شارژ از طریق نرم‌افزار صبا یا نرم‌افزار مربوطه " +chr(9634))
	drawtext(650, line['14'], "اختصاص شارژ از طریق رصدخانه "+chr(9634))
	drawtext(650, line['15'], "سایر " + chr(9634))
	drawtext(650, line['16'], "توضیحات:", 18)
	drawtext(650, line['18'], "مقدار سهم‌آب سالیانه (شارژ سالیانه) در بانک:", 19)
	drawtext(250, line['18'], "متر مکعب", 20)
	drawtext(650, line['19'], "مقدار شارژ مورد نیاز جهت انتقال به کنتور یا جهت ارائه به رصدخانه", 21)
	drawtext(150, line['19'], "متر مکعب")
	drawtext(650, line['20'], "نام و نام خانواگی مالک/نماینده مالکین (متقاضی):")
	drawtext(250, line['20'], "تاریخ:")
	drawtext(50, line['20'], "امضا")
	drawtext(650, line['21'], "نام و نام خانواگی نماینده/وکیل کلیه مالکین چاه:")
	drawtext(250, line['21'], "تاریخ:")
	drawtext(50, line['21'], "امضا")
	drawtext(650, line['22'], "نماینده کارگزار؛")
	drawtext(250, line['22'], "تاریخ:")
	drawtext(50, line['22'], "مهر و امضاٰء")

	painter.end()
	canvas.save('f9' + str(ws.cell(FI, 5).value) +'.png')

