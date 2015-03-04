__author__ = 'Kavin'
__usage__ = 'python MOD_profile_parser.py $Modeller_produced_profile.prf file; ' \
            'script will print lines with E-value = 0.0 to STDOUT'

import sys
import re


def main(filename):
    f = open(filename, 'r')

    for line in f.readlines():
        if line.startswith('   '):
            try:
                data = re.search('(.*0\.0)', line)
                print data.group(1)
            except AttributeError:
                # print(line[0:10]+' -- E-value was not 0')
                pass


if __name__ == "__main__":
    main(sys.argv[1])