from excel_source import *

work_book0 = openpyxl.load_workbook('excel_docs/example.xlsx')
work_book_sheet0 = work_book0['Sheet1']
print(work_book_sheet0['A1'])
# This prints the cell block location w/Sheet info

print(work_book_sheet0['A1'].value)
print(work_book_sheet0['A8'].value)
# this prints the time when the cell was created

print('\n')
work_book1 = work_book_sheet0['B8']
print(work_book1.value)
#This prints the value of the cell

sentence0 = 'On Row ' + str(work_book1.row) + ', Column ' + str(work_book1.column) + ' is ' + str(work_book1.value)
print(sentence0)
# sentence0 will acquire the row & column and tell the user the value of it, by explaining the user in a sentence format

print('\n')
print(work_book_sheet0['C1'].value)
# this just prints the value of the data thats in 'cell#'

print('\n')
print(work_book_sheet0.cell(row=1,column=2))
# aquire the cell info from its respective row & column

print(work_book_sheet0.cell(row=1,column=2).value)
# aquire the cell info with its row & column and prints the value

for index in range(1,7,3):
    print(index,work_book_sheet0.cell(row=index,column=2).value)

print('\n')
for index in range(1,9,2):
    print(index,work_book_sheet0.cell(row=index,column=2).value)
# Prints the sheet's cell index/value by getting its range in and prints its respective info for the user
# to see