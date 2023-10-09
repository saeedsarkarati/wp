from PyQt5.QtCore import Qt, QRect
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
		'18' : 1050,'19' : 1100,'20' : 1150,'21' : 1200,'22' : 1250,'23' : 1300
	}
	canvas = QPixmap(w, h)
	canvas.fill(QColor(255, 255, 255))
	painter = QPainter(canvas)
	font = QFont()
	font.setFamily("IRZar")
	font.setBold(True)
	font.setPointSize(22)
	painter.setFont(font)
	painter.drawText(360, line['0'], "فرم شماره ۹: صدور توکن شارژ")
	painter.drawText(400, line['1'], "(درخواست شارژ کنتور) ")
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
	drawtext(650, line['13'], "نحوه‌ی اختصاص سهم‌آب سالیانه")
	drawtext(650, line['18'], "مشخصات شارژ مورد نیاز:")

	font.setBold(False)
	font.setUnderline(False)
	font.setPointSize(16)
	painter.setFont(font)
	drawtext(650, line['4'], "شهرستان:", 1)
	drawtext(440, line['4'], "دشت:", 2)
	drawtext(240, line['4'], "امور آب تابعه:", 3)
	drawtext(50, line['4'], "نام منبع:", 4)
	drawtext(650, line['5'], "ش. پروانه بهره برداری:", 5)
	drawtext(340, line['5'], "شماره کلاسه پرونده:", 6)
	drawtext(80, line['5'], "نوع مصرف:", 7)
	drawtext(-50, line['5'], " - ", 8)
	drawtext(650, line['8'], "مالک "+chr(9634))
	drawtext(480, line['8'], "نماینده مالک یا تعدادی از مالکین " +chr(9634))
	drawtext(150, line['8'], "نماینده شخص حقوقی " +chr(9634))
	drawtext(650, line['7'], "نام ثبت شده:", 9)
	drawtext(650, line['9'], "نام:", 10)
	drawtext(550, line['9'], "نام خانوداگی:", 11)
	drawtext(350, line['9'], "نام پدر:", 12)
	drawtext(150, line['9'], "شماره شناسنامه:", 13)
	drawtext(650, line['10'], "شماره ملی:", 14)
	drawtext(350, line['10'], "تلفن همراه:", 15)
	drawtext(150, line['10'], "کد پستی", 16)
	drawtext(650, line['11'], "آدرس:", 17)
	drawtext(650, line['12'], "شماره وکالت‌نامه:", 18)
	drawtext(350, line['12'], "تاریخ ثبت وکالتنامه:", 19)
	drawtext(150, line['12'], "شماره دفترخانه:", 20)
	drawtext(650, line['14'], "اختصاص شارژ از طریق نرم‌افزار صبا یا نرم‌افزار مربوطه " +chr(9634))
	drawtext(650, line['15'], "اختصاص شارژ از طریق رصدخانه "+chr(9634))
	drawtext(650, line['16'], "سایر " + chr(9634))
	drawtext(650, line['17'], "توضیحات:", 21)
	drawtext(650, line['19'], "مقدار سهم‌آب سالیانه (شارژ سالیانه) در بانک:", 22)
	drawtext(250, line['19'], "متر مکعب", 23)
	drawtext(650, line['20'], "مقدار شارژ مورد نیاز جهت انتقال به کنتور یا جهت ارائه به رصدخانه", 24)
	drawtext(150, line['20'], "متر مکعب")
	drawtext(650, line['21'], "نام و نام خانواگی مالک/نماینده مالکین (متقاضی):")
	drawtext(250, line['21'], "تاریخ:")
	drawtext(50, line['21'], "امضا")
	drawtext(650, line['22'], "نام و نام خانواگی نماینده/وکیل کلیه مالکین چاه:")
	drawtext(250, line['22'], "تاریخ:")
	drawtext(50, line['22'], "امضا")
	drawtext(650, line['23'], "نماینده کارگزار؛")
	drawtext(250, line['23'], "تاریخ:")
	drawtext(50, line['23'], "مهر و امضاٰء")

	sspixmap = QPixmap("sepehr.png")
	painter.drawPixmap(QRect(10,10,150,150), sspixmap)
	sspixmap = QPixmap("qazvin.png")
	painter.drawPixmap(QRect(800, 10, 150,150), sspixmap)

	painter.end()
	si = str(ws.cell(FI, 6).value)
	i = si.find('/')
	j = si[i+1:].find('/')
	print (si[i+1: i+j+1] )
	canvas.save( si[i+1: i+j+1]+'.png')

