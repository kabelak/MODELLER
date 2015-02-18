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

a = automodel(env, alnfile='CYP2J2_pir_1suo_2.ali',
              knowns='1suo', sequence='P51589',
              assess_methods=(assess.DOPE,
                              # soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 1
a.make()