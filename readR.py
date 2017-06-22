__author__ = 'Kavin'
__usage__ = ''

import sys
import os
from rpy2.robjects import r


def main(file):
    # with open(file, 'r') as contentfile:
    #    content = contentfile.read()
    # print(content)
    r.assign('dataf', os.path.abspath(file))
    r('dc <- read.table(dataf, skip=8, col.names = c("Time", "Distance"))')
    r('d <- dc[,"Distance"]')
    print(r('min(d)')[0])
    print(r('max(d)')[0])
    print(r('mean(d)')[0])
    print(r('median(d)')[0])


if __name__ == "__main__":
    main(sys.argv[1])
