__author__ = 'Kavin'
__usage__ = 'python improp_mod.py <text_file> <excel_file>' \
            '; it is imperative that the excel file has the 4 character long "old" string in the first column,' \
            ' and the 4 character long "new" string in the second column; Script will overwrite original file'

import sys
import xlrd
import fileinput


def inplace_change(filename, old_string, new_string):
    s = open(filename).readlines()
    for line in s:
        if old_string in line.split(' ')[0]:
            print('Changing %s to %s' % (old_string, new_string))
            line = line.replace(old_string, new_string, 1)
            f = open(filename, 'a')
            f.write(line)
            f.flush()
            f.close()
    else:
        print('No occurances of %s found.' % (old_string))


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
        # new = str(str(ws1.cell_value(curr_row, 0))+str(int(ws1.cell_value(curr_row, 1))+43))
        new = str(ws1.cell_value(curr_row, 0))
        print(new)
        replaceAll(file, old, new)
        # inplace_change(file, old, new)
        curr_row += 1


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
