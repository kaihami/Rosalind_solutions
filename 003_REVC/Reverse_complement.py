'''
My solution to Rosalind Bioinformatics Problem
Title: Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind #: 003
URL: http://rosalind.info/problems/revc/
'''

import sys

def Reverse_Complement(fi):
    '''
    :return: The reverse complement
    '''
    ipt_file = open(fi, 'r').read().replace('\n', '')

    complement = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}

    print 'Original:          ', ipt_file

    rev_complement = ''.join([complement[x] for x in ipt_file[::-1]])

    print 'Reverse Complement:', rev_complement

    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(rev_complement)

Reverse_Complement(sys.argv[1])
