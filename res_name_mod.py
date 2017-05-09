__author__ = 'Kavin'
__usage__ = 'python improp_mod.py <text_file> <excel_file>' \
            '; it is imperative that the excel file has the 4 character long "old" string in the first column,' \
            ' and the 4 character long "new" string in the second column; Script will overwrite original file'

import sys
import xlrd
import fileinput

'''
need to do:
create dictionary from excel
open file
read a line
find out if the first 3 characters of the line match any full keys from a dictionary

'''


def replaceAll(filename, old_string, new_string):
    for line in fileinput.input(filename, inplace=1):
        if old_string in line.split(' ')[0]:
            line = line.replace(old_string, new_string, 1)
        sys.stdout.write(line)


def main(file, xlfile):
    wb = xlrd.open_workbook(xlfile)
    ws1 = wb.sheet_by_name('Sheet1')
    num_rows = ws1.nrows - 1
    curr_row = 1
    while curr_row < num_rows:
        old = str(int(ws1.cell_value(curr_row, 1)))
        # print(old)
        new = str(str(ws1.cell_value(curr_row, 0)) + ' ' + str(int(ws1.cell_value(curr_row, 1)) + 43))
        # new = str(int(ws1.cell_value(curr_row, 1))+43)
        # print(new)
        replaceAll(file, old, new)
        # inplace_change(file, old, new)
        curr_row += 1


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
