from excel_source import *

work_book = openpyxl.load_workbook('excel_docs/example.xlsx')
print(work_book.sheetnames)
# This will print to the user the sheet names & their respective numbers
# example -> ['Sheet#', 'Sheet#','Sheet#']

book_sheet = (work_book['Sheet2'])
print(book_sheet)
# Just prints out the sheet info -> <Worksheet 'Sheet#'>

print(type(book_sheet))
# Tells the user the sheet type

print(book_sheet.title)
# Tells the user the sheet title

another_Sheet = work_book.active
print(another_Sheet)
# Just tells the user another sheet#