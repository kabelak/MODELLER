__author__ = 'Kavin'

import sys
import xlrd
import fileinput
import re


def parse_rmsf(filename):
    result = ""
    for line in open(filename).readlines():
        # if (int(line.split(' ')[1][0]) > 2):
        # print(line.split(' ')[1])
        stuff = re.search('.+\d\s\w\w\w\s(\d+)', line)
        if stuff:
            residue = str(stuff.group(1))
            result += residue
            result += ','
    print(result[0:-1])


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


def main(file):
    parse_rmsf(file)


if __name__ == "__main__":
    main(sys.argv[1])
