__author__ = 'Kavin'

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


'''
    wb = xlrd.open_workbook(xlfile)
    # print wb.sheet_names()
    ws1 = wb.sheet_by_name('Sheet1')
    num_rows = ws1.nrows - 1
    curr_row = - 1

    ws2 = wb.sheet_by_name('plamen')
    num_rows2 = ws2.nrows - 1



    atoms = {}
    atomtype = {}
    i = 0
    while curr_row < num_rows:
        curr_row2 = - 1
        while curr_row2 < num_rows2:
            if ws1.cell_value(curr_row, 1) == ws2.cell_value(curr_row2, 0):
                print(str(ws1.cell_value(curr_row, 1)) + "\t" + str(ws2.cell_value(curr_row2, 1)).upper() + "\t" + str(ws1.cell_value(curr_row, 8)) + "\t" + str(i))
            curr_row2 += 1
        curr_row += 1
        i += 1
'''


def main(file):
    wb = xlrd.open_workbook('improp_rn.xlsx')
    ws1 = wb.sheet_by_name('Sheet1')
    num_rows = ws1.nrows - 1
    curr_row = - 1
    while curr_row < num_rows:
        old = str(ws1.cell_value(curr_row, 0))[:4]
        new = str(ws1.cell_value(curr_row, 1))[:4]
        inplace_change(file, old, new)
        curr_row += 1


if __name__ == "__main__":
    main(sys.argv[1])