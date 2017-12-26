'''
My solution to Rosalind Bioinformatics Problem
Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/
'''

import sys
import re
def motif_finder(fi):
    # Find a motif in a sequence, Overlap allowed

    f = open(fi, 'r')
    seq = f.readline().strip('\n')
    motif = f.readline().strip('\n')
    exp = r'(?=(%s))' % (motif)

    result = re.finditer(exp, seq)
    position = []
    for m in result:
        position.append(str(m.start(1) +1))

    print ' '.join(position)
    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(' '.join(position))
motif_finder(sys.argv[1])
