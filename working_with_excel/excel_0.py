from excel_source import *

work_book = openpyxl.load_workbook('excel_docs/example.xlsx')
print(type(work_book))

# this .py just takes the file name and returns the value