__author__ = 'Kavin'

import sys
import xlrd


def main(xlfile):
    wb = xlrd.open_workbook(xlfile)
    # print wb.sheet_names()
    ws1 = wb.sheet_by_name('Sheet1')
    num_rows = ws1.nrows - 1
    # num_cells = ws1.ncols - 1
    curr_row = -1

    atoms = {}
    atomtype = {}
    i = 0
    while curr_row < num_rows:
        curr_row += 1
        #row = ws1.row(curr_row)
        #print row
        #curr_cell = - 1
        #atoms[int(ws1.cell_value(curr_row,0))] = str(ws1.cell_value(curr_row,1))

        print(" " + str(int(ws1.cell_value(curr_row, 0))) + "\t" + str(
            ws1.cell_value(curr_row, 1)) + " \t" + "{0:.3f}".format(
            ws1.cell_value(curr_row, 2)) + "\t" + "{0:.3f}".format(
            ws1.cell_value(curr_row, 3)) + "  " + "{0:.3f}".format(
            ws1.cell_value(curr_row, 4)) + "  " + str(ws1.cell_value(curr_row, 5)) + "  " + str(
            ws1.cell_value(curr_row, 6))[0] + "  " + str(ws1.cell_value(curr_row, 7)) + "  " + "{0:.4f}".format(
            ws1.cell_value(curr_row, 8)))

        i += 1
        '''
        trial = str(ws1.cell_value(curr_row, 5)).upper()
        atomtype[trial] = 1

    for key in atomtype.keys():
        print(key)

        while curr_cell < num_cells:
            curr_cell += 1
            cell_value = ws1.cell_value(curr_row, 1)
            print cell_value


    #for key in atoms.keys():
    #    print(key, atoms[key])

    ws2 = wb.sheet_by_name('Sheet2')
    num_rows2 = ws2.nrows - 1
    curr_row2 = 0


    while curr_row2 < num_rows2:
        curr_row2 += 1
        print(atoms[int(ws2.cell_value(curr_row2,1))]+"\t"+atoms[int(ws2.cell_value(curr_row2,2))])
        #print(int(ws2.cell_value(curr_row2, 1)))
        #print atoms[int(ws2.cell_value(curr_row2, 1))]


    ws3 = wb.sheet_by_name('plamen')
    num_rows3 = ws3.nrows - 1
    curr_row3 = -1
    atomtypes = {}
    while curr_row3 < num_rows3:
        curr_row3 += 1
        atomtypes[str(ws3.cell_value(curr_row3, 0))] = str(ws3.cell_value(curr_row3, 1)).upper()

    for key in atomtypes.keys():
        print(key+" "+atomtypes[key])

'''


if __name__ == "__main__":
    main(sys.argv[1])

