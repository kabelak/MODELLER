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


_root = "/Users/Kavin/phd/MD/Simulation4"
for _sim in ["/Docked_Sims", "/Mut_R111A", "/Mut_R117A", "/Mut_R111A_R117A", "/Mut_quadruple"]:
    # The type here is either wildtype (1) or mutants (0)
    print("%s; Median; Mean; SD" % (_sim))
    type = 0
    if _sim == "/Docked_Sims":
        type = 1

    for o in ['Omega6', 'Omega9', 'Omega12', 'Omega15', 'C19', 'CO2']:
        for i in range(1, 7):
            if type == 1:
                _directory = "/State_%d/007.cpptraj/Distance_FEto%s.%d.old.agr" % (i, o, i)
                _file = _root + _sim + _directory
                _skip = skipvalue(_file)

                print(os.path.abspath(_file))

                r.assign('dataf', os.path.abspath(_file))
                r.assign('skippy', _skip)
                r('dc <- read.table(dataf, skip=skippy, col.names = c("Time", "Distance"))')
                if i == 1:
                    r('d <- dc[,"Distance"]')
                else:
                    r('d <- rbind(d, dc[,"Distance"])')

            for j in range(1, 4):
                _directory = "/State_%d/REPEATS/%d/007.cpptraj/Distance_FEto%s.%d.%d.agr" % (i, j, o, i, j)
                _file = _root + _sim + _directory
                _skip = skipvalue(_file)
                r.assign('dataf', os.path.abspath(_file))
                r.assign('skippy', _skip)
                r('dc <- read.table(dataf, skip=skippy, col.names = c("Time", "Distance"))')

                if type == 1:
                    r('d <- rbind(d, dc[,"Distance"])')
                else:
                    if j == 1:
                        r('d <- dc[,"Distance"]')
                    else:
                        r('d <- rbind(d, dc[,"Distance"])')

                        # print("Pose: %d; %s" % (i, o))
                        # print("Median post 100ns:", r('median(d)')[0])
                        # print("Pose %d; %f; %s" % (i, r('median(d)')[0], o))
                        # print("Median post 100ns:", r('median(d)')[0])
        # print("Pose %d; %f; %s" % (i, r('median(d)')[0], o))

        print("%s; %f; %f; %f" % (o, r('median(d)')[0], r('mean(d)')[0], r('sd(d)')[0]))
        # r('hist(d)')
        # input("\nPress Enter to continue.")

        # Save the dataframe as .Rdata for future use
        Rdataout = _root + _sim + "/" + o + "combined.Rdata"
        r.assign('fileout', Rdataout)
        r('save(d, file=fileout)')
