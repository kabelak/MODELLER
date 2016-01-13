__author__ = 'Kavin'
__usage__ = 'For use when analysing text files created using VMD; For instance, following the simulation of a CYP+ARA docked complex,' \
            'one can use VMD to create a list of atoms which are found within 3A of each atom of ARA; this file (per atom of ARA) can' \
            'be run through this script and thus the atoms within 3A which appear within the frames are ranked according to frequency.'

import sys
import re
import operator


def main(atomfile):
    atmlist = {}
    with open(atomfile, 'rU') as f:
        for line in f:
            for i in line.split():
                if i in atmlist:
                    atmlist[i] = atmlist[i] + 1
                else:
                    atmlist[i] = 1

    fname = re.search('(.*)\.(\w*)', atomfile)
    fname2 = str(fname.group(1)) + '_processed.' + str(fname.group(2) + '.txt')
    with open(fname2, "w") as out:
        for w in sorted(atmlist, key=atmlist.get, reverse=True):
            out.write(str(w) + " : " + str(atmlist[w]) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])