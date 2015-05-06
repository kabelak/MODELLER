__author__ = 'Kavin'
__usage__ = 'python improp_mod.py <text_file> <excel_file>' \
            '; it is imperative that the excel file has the 4 character long "old" string in the first column,' \
            ' and the 4 character long "new" string in the second column; Script will overwrite original file'

import sys
import xlrd


def inplace_change(filename, old_string, new_string):
    s = open(filename).read()
    if old_string in s:
        print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
        s = s.replace(old_string, new_string)
        f = open(filename, 'w')
        f.write(s)
        f.flush()
        f.close()
    else:
        print 'No occurances of "{old_string}" found.'.format(**locals())


def main(file, xlfile):
    wb = xlrd.open_workbook(xlfile)
    ws1 = wb.sheet_by_name('Sheet1')
    num_rows = ws1.nrows - 1
    curr_row = - 1
    while curr_row < num_rows:
        old = str(ws1.cell_value(curr_row, 0))[:4]
        new = str(ws1.cell_value(curr_row, 1))[:4]
        inplace_change(file, old, new)
        curr_row += 1


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])