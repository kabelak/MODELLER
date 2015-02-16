__author__ = 'Kavin'

import sys

from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od

env = environ()
log.verbose()

#env.io.atom_files_directory = ['.', './pdbfiles/1PO5']
# Read in HETATM records from template PDBs
#env.io.hetatm = True

a = automodel(env, alnfile='CYP2J2_pir_1PO5.ali',
              knowns='1PO5', sequence='P51589',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 1
a.make()