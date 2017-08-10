__author__ = 'Kavin'
__usage__ = ''

from openpyxl import *
from rpy2.robjects import r


def skipvalue(_filename):
    _skip = 0
    if "Mut" in _filename:
        _skip = 10008
    else:
        _skip = 5008

    return _skip


for o in ['Omega6', 'Omega9', 'Omega12', 'Omega15', 'C19', 'CO2']:
    for i in range(1, 7):
        _file = "/Users/Kavin/phd/MD/Simulation4/Docked_Sims/State_%d/007.cpptraj/Distance_FEto%s.%d.old.agr" % (
        i, o, i)
        _skip = skipvalue(_file)
        r.assign('dataf', os.path.abspath(_file))
        r.assign('skippy', _skip)
        r('dc <- read.table(dataf, skip=skippy, col.names = c("Time", "Distance"))')
        r('d <- dc[,"Distance"]')
        # print(r('median(d)')[0])

        for j in range(1, 3):
            _file = "/Users/Kavin/phd/MD/Simulation4/Docked_Sims/State_%d/REPEATS/%d/007.cpptraj/Distance_FEto%s.%d.%d.agr" % (
            i, j, o, i, j)
            _skip = skipvalue(_file)
            r.assign('dataf', os.path.abspath(_file))
            r.assign('skippy', _skip)
            r('dc <- read.table(dataf, skip=skippy, col.names = c("Time", "Distance"))')
            r('d <- rbind(d, dc[,"Distance"])')

        print("Pose: %d; Omega: %s" % (i, o))
        print("Median post 100ns:", r('median(d)')[0])
