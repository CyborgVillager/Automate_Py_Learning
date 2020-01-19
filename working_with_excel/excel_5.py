'''
Excel_4 main function
    -Getting Rows & Columns from Sheet info Part 2
'''

from excel_source import *

work_book = openpyxl.load_workbook('excel_docs/example.xlsx')
work_book_sheet = work_book.active


print(next(work_book_sheet.columns))
# Updated solution aquired from:
# https://stackoverflow.com/questions/42603795/typeerror-generator-object-is-not-subscriptable
print('\n')

for cell_Obj in list(work_book_sheet.columns)[1]:
    print(cell_Obj.value)

# this prints out food items


for cell_Obj in list(work_book_sheet.columns)[2]:
    print(cell_Obj.value)
# this prints out data #'s with the



for cell_Obj in next(work_book_sheet.columns):
    print(cell_Obj.value)
# this prints out row time stamps