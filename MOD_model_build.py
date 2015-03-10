__author__ = 'Kavin'

import sys
from modeller import *
from modeller.automodel import *
from modeller import soap_protein_od

env = environ()
log.verbose()

env.io.atom_files_directory = ['./pdbfiles']
# Read in HETATM records from template PDBs
# HETATM needs to be identified by '.' per HETATM (eg: HEM = 1 '.') in .ali file,
# for both sequence and structure
env.io.hetatm = True

a = automodel(env, alnfile='CYP2J2_pir_trim_1SUO_trim.ali',
              knowns='1SUO', sequence='CYP2J2',
              assess_methods=(assess.DOPE,
                              soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()