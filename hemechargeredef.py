__author__ = 'Kavin'

import sys
import xlrd


def main(xlfile):
    wb = xlrd.open_workbook(xlfile)
    # print wb.sheet_names()
    ws1 = wb.sheet_by_name('gr54a7_hem')
    num_rows = ws1.nrows
    curr_row = 1

    ws2 = wb.sheet_by_name('gr54a7_shah')
    num_rows2 = ws2.nrows

    # atoms = {}
    #atomtype = {}
    #i = 0
    while curr_row < num_rows:
        curr_row2 = 1
        while curr_row2 < num_rows2:
            if ws1.cell_value(curr_row, 1) == ws2.cell_value(curr_row2, 1):
                print(str(ws1.cell_value(curr_row, 1)) + "\t" + str(ws1.cell_value(curr_row, 2)) + "\t" + str(
                    ws2.cell_value(curr_row2, 2)) + "\t" + str(int(
                    ws1.cell_value(curr_row, 4))))
            curr_row2 += 1
        curr_row += 1
        #i += 1


if __name__ == "__main__":
    main(sys.argv[1])

