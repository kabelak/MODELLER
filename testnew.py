__author__ = 'Kavin'
__usage__ = ''

import sys
import re
import argparse
import os
from openpyxl import *
from rpy2.robjects import r

_root = "/Users/Kavin/phd/MD/Simulation4"
_sim = "/Docked_Sims"

for o in ['Omega6', 'Omega9', 'Omega12', 'Omega15', 'C19', 'CO2']:
    for i in range(1, 7):
        _directory = "/State_%d/007.cpptraj/Distance_FEto%s.%d.old.agr" % (i, o, i)
        _file = _root + _sim + _directory
        print(_file)
