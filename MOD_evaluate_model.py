__author__ = 'Kavin'

import sys
import re
from modeller import *
from modeller.scripts import complete_pdb

def ModelEval(pdb):
    # Builds a DOPE profile based on pdb file
    log.verbose()    # request verbose output
    env = environ()
    env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
    env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

    # read model file
    mdl = complete_pdb(env, pdb)

    # Assess with DOPE:
    s = selection(mdl)   # all atom selection
    fname = re.search('/?(\w*)\.(\w*)$', sys.argv[1]) # Create output filename
    s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file=str(fname.group(1)+'.profile'),
                  normalize_profile=True, smoothing_window=15)

def main(pdb):
    ModelEval(pdb)

if __name__ == "__main__":
    main(sys.argv[1])