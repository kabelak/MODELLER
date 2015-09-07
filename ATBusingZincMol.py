__author__ = 'Kavin'
__usage__ = 'Looks within an excel sheet; in one worksheet, there is a straight name comparison from Zinc to ATB; in two others, there' \
            'is the mol2 file for each format; We will use all data from ATB, except charges which will be taken from Zinc;' \
            'Due to the difference in atom nomenclature, we will first parse ATB, say atom H1, find the corresponding atom name in ' \
            'Zinc, say H20, parse Zinc to find the charge for H20 and add it to the ATB before printing the line out'
import sys
import xlrd


def main(xlfile):
    wb = xlrd.open_workbook(xlfile)

    # # First create a dict to translate ATB names to Zinc
    ws3 = wb.sheet_by_name('Zn2ATB')
    atbatoms = {}
    curr_row = 1
    while curr_row < ws3.nrows:
        #rowd = ws3.row(curr_row)
        atbatoms[ws3.cell_value(curr_row, 1)] = ws3.cell_value(curr_row, 0)
        curr_row += 1

    ## Next initialise the two worksheets
    ws1 = wb.sheet_by_name('ATB')
    ws2 = wb.sheet_by_name('Zinc')

    ## Read in the charges for each atom name in Zinc
    zncharge = {}
    curr_row = 1
    while curr_row < ws2.nrows:
        zncharge[ws2.cell_value(curr_row, 1)] = ws2.cell_value(curr_row, 8)
        curr_row += 1

    ## Now read in the ATB lines and print line by line, being careful to replace the charges
    curr_row = 1
    while curr_row < ws1.nrows:
        znval = atbatoms[ws1.cell_value(curr_row, 1)]
        print(" " + str(int(ws1.cell_value(curr_row, 0) - 1)) + "\t" + str(
            ws1.cell_value(curr_row, 1)) + " \t" + "{0:.3f}".format(
            ws1.cell_value(curr_row, 2)) + "\t" + "{0:.3f}".format(
            ws1.cell_value(curr_row, 3)) + "  " + "{0:.3f}".format(
            ws1.cell_value(curr_row, 4)) + "  " + str(ws1.cell_value(curr_row, 5)) + "  " + str(
            ws1.cell_value(curr_row, 6))[0] + "  " + str(ws1.cell_value(curr_row, 7)) + "  " + "{0:.4f}".format(
            zncharge[znval]))
        curr_row += 1

    ## Read in and print the connect lines, modifying to account for missing H29
    ws4 = wb.sheet_by_name('connect')
    curr_row = 0
    while curr_row < ws4.nrows:
        print(str(int(ws4.cell_value(curr_row, 0)) - 1) + "\t" + str(int(ws4.cell_value(curr_row, 1)) - 1) + "\t" + str(
            int(ws4.cell_value(curr_row, 2)) - 1) + "\t" + str(int(ws4.cell_value(curr_row, 3))))
        curr_row += 1


if __name__ == "__main__":
    main(sys.argv[1])

