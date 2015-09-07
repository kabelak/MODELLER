__author__ = 'Kavin'

import sys
import xlrd


def main(xlfile):
    wb = xlrd.open_workbook(xlfile)
    ws = wb.sheet_by_name('Sheet1')

    curr_row = 1
    while curr_row < ws.nrows:
        if (curr_row % 2 == 0):
            print(" " + str(ws.cell_value(curr_row, 2)) + " " + str(ws.cell_value(curr_row, 3)) + " " + str(
                ws.cell_value(curr_row, 4)) + " " + str(ws.cell_value(curr_row, 5)) + " " + str(
                ws.cell_value(curr_row, 6)) + " " + str(ws.cell_value(curr_row, 7)))
        curr_row += 1

    print("\n\nNOW THE ODD\n\n")
    curr_row = 1
    while curr_row < ws.nrows:
        if (curr_row % 2 != 0):
            print(" " + str(ws.cell_value(curr_row, 2)) + " " + str(ws.cell_value(curr_row, 3)) + " " + str(
                ws.cell_value(curr_row, 4)) + " " + str(ws.cell_value(curr_row, 5)) + " " + str(
                ws.cell_value(curr_row, 6)) + " " + str(ws.cell_value(curr_row, 7)))
        curr_row += 1


if __name__ == "__main__":
    main(sys.argv[1])