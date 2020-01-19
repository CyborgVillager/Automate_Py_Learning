from excel_source import *

work_book = openpyxl.load_workbook('excel_docs/example.xlsx')
# old code -> work_book.get_sheet_by_name('Sheet#')
# new code -> work_book['Sheet#']
current_sheet_working_on = 'Sheet1'
work_book_sheet0 = work_book[current_sheet_working_on]

print(work_book_sheet0.max_row)
work_book_sheet_row = work_book_sheet0.max_row
# this will print the max # of rows for Sheet1

print(work_book_sheet0.max_column)
work_book_sheet_column = work_book_sheet0.max_column
# this will print out the max # of columns for Sheet1

# makes space between the max column & row and the sentences
def space():
    space = '\n'
    print(space)

# func for sentence / aquire info on max row & column and print its results to the user
def sentence():
    sentence0 = 'Work Book ' + current_sheet_working_on + ' max row is ' + str(work_book_sheet_row)
    sentence1 = 'It\'s max row is for '+ current_sheet_working_on + ' is ' + str(work_book_sheet_column)
    print(sentence0)

    print(sentence1)

def main():
    space()
    sentence()


main()