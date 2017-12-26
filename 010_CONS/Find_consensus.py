'''
My solution to Rosalind Bioinformatics Problem
Title: Consensus and Profile
Rosalind ID: CONS
Rosalind #: 010
URL: http://rosalind.info/problems/cons/
'''

import sys
import pandas as pd

def parse(fi):
    # Parse the input fasta file
    
    # Return: a dict with key = sequence header, value = list of nucleotides
    tmp = {}

    for x in xrange(0, len(fi)):
        if fi[x].startswith('>'):
            header = fi[x]
            tmp[header] = ''
        else:
            tmp[header] += fi[x]
    seqs = {}

    for k,v in tmp.items():
        seqs[k] = [x for x in v]
    return seqs

def Consensus(fi):
    # Return a dataframe, Row = nucleotide, Column = position in the sequence
    # Using pandas, find max value in a column if idxmax, count frequency in each row with a mask and a sum().
    seq = open(fi, 'r').read().split('\n')

    s = parse(seq)

    df = pd.DataFrame.from_dict(s, orient = 'index')

    order = 'A C G T'.split()
    df2 = pd.DataFrame(columns = 'A C T G'.split())
    s = ''
    for letter in order:

        s += letter + ': '
        o = ([str(x) for x in (df == letter).sum().values]) # Count frequency a letter
        df2[letter] = (df == letter).sum().T
        s += ' '.join(o)
        if letter != 'T':
            s+= '\n'

    Motif_seq = ''.join(df2.idxmax(axis=1).values) # Find consensus 

    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(Motif_seq)
        f.write('\n')
        f.write(s)

Consensus(sys.argv[1])
