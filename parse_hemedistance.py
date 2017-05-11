__author__ = 'Kavin'
__usage__ = ''

import sys
import re
import argparse
import os


def check_range(arg):  # Function to ensure correct range of IRE Length is input at the command prompt
    try:
        value = int(arg)
    except ValueError as err:
        raise argparse.ArgumentTypeError(str(err))
    if value < 1 or value > 30:
        message = "Expected length between 1 and 30 inclusive, received value = {}".format(value)
        raise argparse.ArgumentTypeError(message)
    return value


def main(argv):
    #   Parse input arguments
    parser = argparse.ArgumentParser(description='Parses Fe-Omega/Carbon Atom distance files',
                                     usage='python3 parse_hemedistance.py <file> <cutoff>')
    parser.add_argument('file', help='Distance file')
    parser.add_argument('cutoff', type=check_range, help='Cut-off value',
                        default=6, nargs=1)
    args = parser.parse_args()

    #   Check that file is input
    if not args.file:
        parser.error('Please specify a distance file')

    with open(args.file, "r") as df:

        #   Introduce counters
        total_frames = 0
        relevant_frames = 0

        #   Process file line by line
        for _line in df.readlines():
            dist_cols = re.search('^\s*(\d+)\.000\s*(\d+\.\d+)', _line)
            if dist_cols:
                total_frames += 1
                if float(dist_cols.group(2)) < args.cutoff[0]:
                    relevant_frames += 1

        print('\tFile Name:\t', args.file, '\n',
              '\tTotal Frames:\t', total_frames, '\n',
              '\t< cutoff:\t', relevant_frames, '\n',
              '\t% < cutoff:\t', (relevant_frames / total_frames * 100))


if __name__ == "__main__":
    main(sys.argv)
