__author__ = 'Kavin'

import sys
import os
import re
from modeller import *

def ModBuildProf(inputalign):
    # Will build a profile based on the input PIR formatted sequence file

    log.verbose()
    env = environ()
    #-- Prepare the input files
    #-- Read in the sequence database
    sdb = sequence_db(env)
    if os.path.exists('pdb_95.bin'):
        pass
    else:
        sdb.read(seq_database_file='pdb_95.pir', seq_database_format='PIR',
                 chains_list='ALL', minmax_db_seq_len=(30, 4000), clean_sequences=True)
        #-- Write the sequence database in binary form
        print "Converting pdb_95 file for input"
        sdb.write(seq_database_file='pdb_95.bin', seq_database_format='BINARY',
                  chains_list='ALL')

    #-- Now, read in the binary database
    sdb.read(seq_database_file='pdb_95.bin', seq_database_format='BINARY',
             chains_list='ALL')

    #-- Read in the target sequence/alignment
    aln = alignment(env)
    aln.append(file=inputalign, alignment_format='PIR', align_codes='ALL')

    #-- Convert the input sequence/alignment into
    #   profile format
    prf = aln.to_profile()

    #-- Scan sequence database to pick up homologous sequences
    prf.build(sdb, matrix_offset=-450, rr_file='${LIB}/blosum62.sim.mat',
              gap_penalties_1d=(-500, -50), n_prof_iterations=1,
              check_profile=False, max_aln_evalue=0.001, gaps_in_target=False)

    #-- Write out the profile in text format
    fname = re.search('/?(\w*)\.(\w*)$', inputalign)
    outprfname = str(fname.group(1)) + '_profile.prf'
    prf.write(file=outprfname, profile_format='TEXT')

    #-- Convert the profile back to alignment format
    aln = prf.to_alignment()

    #-- Write out the alignment file
    outaliname = str(fname.group(1)) + '_profile.ali'
    aln.write(file=outaliname, alignment_format='PIR')

def main(file):
    ModBuildProf(file)


if __name__ == "__main__":
    main(sys.argv[1])