# import openpyxl module 
import openpyxl 
  
# Call a Workbook() function of openpyxl  
# to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
# Get workbook active sheet   
# from the active attribute.  
sheet = wb.active 
  
# Once have the Worksheet object, 
# one can get its name from the 
# title attribute. 
sheet_title = sheet.title 
  
print("active sheet title: " + sheet_title) 
sheet.title = '10'
print (sheet.title)
