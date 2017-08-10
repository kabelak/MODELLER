__author__ = 'Kavin'
__usage__ = 'python3 parse_rmsf.py RMSF_FILE <min_rmsf_value_to_pickup> ' \
            'Remember that the residue number shown will be the "PDB" number ' \
            'and NOT the "real" residue number shown on the RMSF plot' \
            'If its not working, try to include: ' \
            ' export PYTHONPATH=$PYTHONPATH:/usr/lib/modeller9.14/lib/x86_64-intel8' \
            ' export PYTHONPATH=$PYTHONPATH:/usr/lib/modeller9.14/modlib/'

import sys
import xlrd
import fileinput
import re


def parse_rmsf(filename, rmsf):
    result = "select :"
    for line in open(filename).readlines():
        # if (int(line.split(' ')[1][0]) > 2):
        # print(line.split(' ')[1])
        stuff = re.search('\s*(\d+)\..*\s*(\d+\.\d\d)', line)
        # print(stuff)
        # print(float(stuff.group(2)))
        if stuff and float(stuff.group(2)) > float(rmsf):
            # print('%s is %s' % (stuff.group(1), stuff.group(2)))
            # residue = str(int(stuff.group(1)) - 43)
            residue = str(int(stuff.group(1)))
            result += residue
            result += ','
    print(result[0:-1])
    #print(result)


'''
        if line.split(' ')[1] == int:
            print(line.split(' ')[0])


    fname = re.search('(.*)\.(\w*)', atomfile)
    fname2 = str(fname.group(1)) + '_processed.' + str(fname.group(2) + '.txt')
    with open(fname2, "w") as out:
        for w in sorted(atmlist, key=atmlist.get, reverse=True):
            out.write(str(w) + " : " + str(atmlist[w]) + "\n")





        #print(line.split(' ')[0][0:2])
'''


def main(file, rmsf):
    parse_rmsf(file, rmsf)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
