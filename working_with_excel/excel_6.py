# Source Code
from excel_source import *

# Allows countyData from funct work_book_load to be loaded into
# funct census_Results

work_book = openpyxl.load_workbook('excel_docs/censuspopdata.xlsx')
work_book_sheet = work_book['Population by Census Tract']
countyData = {}

def loading():
    print('Opening Workbook...')
    # Time Delay
    time.sleep(1)
    print('Reading Rows.')
    time.sleep(2)
    print('Reading Rows..')
    time.sleep(1)
    print('Reading Rows...')

# Obj Fill countyData with each county's respective pop & tracts

def data_gather():
    for row in range(2, work_book_sheet.max_row + 1):
        # Each row in the spreadsheet has data for one census tract.
        state = work_book_sheet['B' + str(row)].value
        county = work_book_sheet['C' + str(row)].value
        population = work_book_sheet['D' + str(row)].value

        # Make sure the key for this state exists.
        countyData.setdefault(state, {})
        # Make sure the key for this county in this state exists.
        countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

        # Each row represents 1 census tract +=1
        countyData[state][county]['tracts'] += 1
        # Increase the county population  in the census tract
        countyData[state][county]['pop'] += int(population)


def results():
    # Open a new text file and write the contents of countyData @ census_data/census2010 to it.
    print('Writing Results...')
    resultFile = open('census_data/census2010.py', 'w')
    resultFile.write('allData = ' + pprint.pformat(countyData))
    resultFile.close()
    print('Done.')

def main():
    loading()
    data_gather()
    results()

main()


