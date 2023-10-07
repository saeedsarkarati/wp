
import openpyxl 
wb = openpyxl.Workbook() 
sheet = wb.active 
  
# Cell objects also have row, column 
# and coordinate attributes that provide 
# location information for the cell. 
  
# Note: The first row or column integer 
# is 1, not 0. Cell object is created by 
# using sheet object's cell() method. 
c1 = sheet.cell(row = 1, column = 10) 
sheet.title = 'سعید'
# writing values to cells 
c1.value = "ANKIT"
  
c2 = sheet.cell(row= 1 , column = 2) 
c2.value = "RAI"
  
# Once have a Worksheet object, one can 
# access a cell object by its name also. 
# A2 means column = 1 & row = 2. 
c3 = sheet['A4'] 
c3.value = "RAHUL"
  
# B2 means column = 2 & row = 2. 
c4 = sheet['B3'] 
c4.value = "RAI"

# Sheets can be added to workbook with the 
# workbook object's create_sheet() method.  

wb.create_sheet(index = 1 , title = "sheet2") 
sheet = wb.active 
print ('ss', sheet.title, wb)
for sh in wb:
	print (sh)
# ~ wb.active = 0
# ~ wb.active = 1
# ~ wb.active = wb['sheet2']
wb.active = wb['سعید']
sheet = wb['sheet2']
c1 = sheet.cell(row = 1, column = 1) 
# writing values to cells 
c1.value = "یک"
c2 = sheet.cell(row= 1 , column = 2) 
c2.value = "دو"

# Anytime you modify the Workbook object 
# or its sheets and cells, the spreadsheet 
# file will not be saved until you call 
# the save() workbook method. 
for row in sheet.iter_rows(min_row=1, max_col=3, max_row=2):
	for cell in row:
		# ~ print(cell.value)
		cell.value = '1'

# ~ for col in sheet.iter_cols(min_row=1, max_col=3, max_row=2):
	# ~ for cell in col:
		# ~ print(cell)

print (list(sheet.values))
ss = list(list(x) for x in sheet.values)
print ('ss' , ss)
for row in sheet.values:
	print (row, type(row))
	for value in row:
		print(value)

print('-----------')
for x in ss:
	for y in x:
		print(y)
	print()


wb.save("demo_addsheets.xlsx") 
	
