__author__ = 'Kavin'
__usage__ = 'python MOD_salign.py pdb+chains; Ensure the script is modified with the correct alignment file ' \
            '(See ModSalignMult)'

import sys
from modeller import *
from modeller.automodel import *
from modeller import soap_protein_od
from MOD_pdb_compare import pdbDownload

log.verbose()

def ModSalign(pdblist):
    outname = 'salign_'+("_".join("%s%s" % (key,pdblist[key]) for key in pdblist.keys()))

    env = environ()
    env.io.atom_files_directory = ['./pdbfiles']
    env.io.hetatm = True

    aln = alignment(env)
    for pdb in pdblist.keys():
        m = model(env, file=pdb, model_segment=('FIRST:'+pdblist[pdb], 'LAST:'+pdblist[pdb]))
        aln.append_model(m, atom_files=pdb, align_codes=pdb+pdblist[pdb])

    for (weights, write_fit, whole) in (((1., 0., 0., 0., 1., 0.), False, True),
                                        ((1., 0.5, 1., 1., 1., 0.), False, True),
                                        ((1., 1., 1., 1., 1., 0.), True, False)):
        aln.salign(rms_cutoff=3.5, normalize_pp_scores=False,
                   rr_file='$(LIB)/as1.sim.mat', overhang=30,
                   gap_penalties_1d=(-450, -50),
                   gap_penalties_3d=(0, 3), gap_gap_score=0, gap_residue_score=-100,
                   dendrogram_file=str(outname+'.tree'),
                   alignment_type='tree', # If 'progresive', the tree is not
                                          # computed and all structures will be
                                          # aligned sequentially to the first
                   feature_weights=weights, # For a multiple sequence alignment only
                                            # the first feature needs to be non-zero
                   improve_alignment=True, fit=True, write_fit=write_fit,
                   write_whole_pdb=whole, output='ALIGNMENT QUALITY')

    aln.write(file=str(outname+'.pap'), alignment_format='PAP')
    aln.write(file=str(outname+'.ali'), alignment_format='PIR')

    aln.salign(rms_cutoff=1.0, normalize_pp_scores=False,
               rr_file='$(LIB)/as1.sim.mat', overhang=30,
               gap_penalties_1d=(-450, -50), gap_penalties_3d=(0, 3),
               gap_gap_score=0, gap_residue_score=0, dendrogram_file=str(outname+'_QUAL.tree'),
               alignment_type='progressive', feature_weights=[0]*6,
               improve_alignment=False, fit=False, write_fit=True,
               write_whole_pdb=False, output='QUALITY')

    return str(outname+'.ali')



def ModSalignMult(salignf):
    env = environ()
    env.libs.topology.read(file='$(LIB)/top_heav.lib')
    env.io.hetatm = True

    # Read aligned structure(s):
    aln = alignment(env)
    aln.append(file=salignf, align_codes='all')
    aln_block = len(aln)

    # Read aligned sequence(s):
    aln.append(file='../Sequences/CYP2J2_pir_trim.txt', align_codes='CYP2J2')

    # Structure sensitive variable gap penalty sequence-sequence alignment:
    aln.salign(output='', max_gap_length=20,
               gap_function=True,   # to use structure-dependent gap penalty
               alignment_type='PAIRWISE', align_block=aln_block,
               feature_weights=(1., 0., 0., 0., 0., 0.), overhang=0,
               gap_penalties_1d=(-450, 0),
               gap_penalties_2d=(0.35, 1.2, 0.9, 1.2, 0.6, 8.6, 1.2, 0., 0.),
               similarity_flag=True)

    aln.write(file=str(salignf[:-4]+'_mult.ali'), alignment_format='PIR')
    aln.write(file=str(salignf[:-4]+'_mult.pap'), alignment_format='PAP')

    return str(salignf[:-4]+'_mult.ali')



def ModModelCreate(salign_multf, pdblist):
    env = environ()
    # Read in HETATM records from template PDBs
    # HETATM needs to be identified by '.' per HETATM (eg: HEM = 1 '.') in .ali file,
    # for both sequence and structure
    env.io.hetatm = True
    a = automodel(env, alnfile=salign_multf,
                  knowns=pdblist, sequence='CYP2J2',
                  assess_methods=(assess.DOPE,
                                  soap_protein_od.Scorer(),
                                  assess.GA341))
    a.starting_model = 1
    a.ending_model = 10
    a.make()


def main():
    try:
        file_input = sys.argv[1:]
    except IndexError:
        print __usage__
        sys.exit()

    # Extract PDB id and Chain information
    pdb_dict = {}
    pdb_list = ()
    for arg in file_input:
        # Split into PDB id and Chain id
        pdb_id = arg.lower()[:4]
        chain_id = arg.upper()[4:]
        pdb_dict[pdb_id] = chain_id
        pdb_list += (arg.lower()[:4]+arg.upper()[4:],)

    # Download the pdbs, if required
    # print pdb_list
    pdbDownload(pdb_dict.keys(), hostname="ftp.wwpdb.org", directory="/pub/pdb/data/structures/all/pdb/", prefix="pdb",
                suffix=".ent.gz")

    # Align input PDB files according to selected chains
    pdb_align = ModSalign(pdb_dict)
    # raw_input("MODSalign")

    # Align PDB alignment with sequence (in PIR format)
    full_align = ModSalignMult(pdb_align)

    raw_input("Check the alignment file %s and press any key to continue to modelling step" % full_align)

    # Create models based on ModSalignMult alignment
    ModModelCreate(full_align, pdb_list)


if __name__ == "__main__":
    main()