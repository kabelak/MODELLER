__author__ = 'Kavin'

import sys
import pylab
import modeller

def r_enumerate(seq):
    """Enumerate a sequence in reverse order"""
    # Note that we don't use reversed() since Python 2.3 doesn't have it
    num = len(seq) - 1
    while num >= 0:
        yield num, seq[num]
        num -= 1

def get_profile(profile_file, seq):
    """Read `profile_file` into a Python array, and add gaps corresponding to
       the alignment sequence `seq`."""
    # Read all non-comment and non-blank lines from the file:
    f = file(profile_file)
    vals = []
    for line in f:
        if not line.startswith('#') and len(line) > 10:
            spl = line.split()
            vals.append(float(spl[-1]))
    # Insert gaps into the profile corresponding to those in seq:
    for n, res in r_enumerate(seq.residues):
        for gap in range(res.get_leading_gaps()):
            vals.insert(n, None)
    # Add a gap at position '0', so that we effectively count from 1:
    vals.insert(0, None)
    return vals

def main(): # put in alignf, templatef, modelf
    alignf = 'CYP2J2_pir_1suo.ali'
    templatef = '1suo.profile'
    modelf = 'B99990001_1suo.profile'

    e = modeller.environ()
    a = modeller.alignment(e, file=alignf)

    template = get_profile(templatef, a['1suo'])  # change 1PO5 to required name
    model = get_profile(modelf, a['P51589']) # change P51589 to required name

    # Plot the template and model profiles in the same plot for comparison:
    pylab.figure(1, figsize=(10,6))
    pylab.xlabel('Alignment position')
    pylab.ylabel('DOPE per-residue score')
    pylab.plot(model, color='red', linewidth=2, label='Model')
    pylab.plot(template, color='green', linewidth=2, label='Template')
    pylab.legend()
    pylab.savefig(str(templatef[:-8] + '_based_' + modelf[:-8] + '_model.png'), dpi=65)

if __name__ == "__main__":
    main()
