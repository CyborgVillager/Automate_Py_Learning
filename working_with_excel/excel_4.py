'''
Excel_4 main function
    -Getting Rows & Columns from Sheet info
'''

from excel_source import *

work_book = openpyxl.load_workbook('excel_docs/example.xlsx')
work_book_sheet = work_book['Sheet1']
print(tuple(work_book_sheet['A1':'D3']))
# this prints out the cell sheet from A1 to D3

print('\n')

for row_Of_Cell_Objects in work_book_sheet['A1':'D3']:
    for cell_Obj in row_Of_Cell_Objects:
        print(cell_Obj.coordinate,cell_Obj.value)
    print('----END OF ROW----')

# this aquires the cell objects from A1 - D3 and makes a 'container of each subject with their
# corrisponding data