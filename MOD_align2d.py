__author__ = 'Kavin'

import sys
import re
from modeller import *

def ModAlign2D(align,pdb):
    # Will build an alignment based on the PIR formatted input sequence (align) and
    # chosen structure file (pdb)
    env = environ()
    aln = alignment(env)
    fname = re.search('/?(\w*)\.(\w*)$', align)
    pname = re.search('/?(\w*)\.(\w*)$', pdb)

    mdl = model(env, file=pdb, model_segment=('FIRST:A','LAST:A'))
    aln.append_model(mdl, align_codes=pname.group(1), atom_files=pdb)
    aln.append(file=align, align_codes='P51589')
    aln.align2d()

    outname = str(fname.group(1)+'_'+pname.group(1))

    aln.write(file=str(outname+'.ali'), alignment_format='PIR')
    aln.write(file=str(outname+'.pap'), alignment_format='PAP')

def main(align,pdb):
    ModAlign2D(align, pdb)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
