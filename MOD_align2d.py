__author__ = 'Kavin'

import sys
import re
from modeller import *

def ModAlign2D(align,pdb):
    # Will build an alignment based on the PIR formatted input sequence (align) and
    # chosen structure file (pdb)
    env = environ()
    aln = alignment(env)
    env.io.atom_files_directory = './pdbfiles'
    fname = re.search('/?(\w*)\.(\w*)$', align)
    # pname = re.search('/?(\w*)\.(\w*)$', pdb)

    mdl = model(env, file=pdb, model_segment=('FIRST:A','LAST:A'))
    aln.append_model(mdl, align_codes=pdb, atom_files=pdb)
    aln.append(file=align, align_codes='CYP2J2')
    aln.align2d()

    outname = str(fname.group(1) + '_' + pdb)

    aln.write(file=str(outname + '_trim.ali'), alignment_format='PIR')
    aln.write(file=str(outname + '_trim.pap'), alignment_format='PAP')

def main(align,pdb):
    ModAlign2D(align, pdb)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
