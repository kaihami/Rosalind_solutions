'''
My solution to Rosalind Bioinformatics Problem
Title: Computing GC Content
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc/
'''

import sys

def parse(fi):
    # Parse the input fasta file
    # Calculate GC content
    # Return: a dict with key = sequence header, value = GC content in percentage
    seqs = {}

    for x in xrange(0, len(fi)):
        if fi[x].startswith('>'):
            header = fi[x]
            seq = ''
            for y in xrange(x+1, len(fi)):
                if fi[y].startswith('>') or y == len(fi)-1:
                    GC = seq.count('G') + seq.count('C')
                    percentage = (float(GC)/ float(len(seq)))*100.00

                    seqs[header] = percentage
                    break
                else:
                    seq += fi[y]
    return seqs

def GC(fi):
    fastas = open(fi, 'r').read().split('\n')
    a = parse(fastas)
    max_key = max(a.iterkeys(), key=lambda k: a[k])
    max_val = a[max_key]
    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(max_key.replace('>', ''))
        f.write('\n')
        f.write(str(max_val))


GC(sys.argv[1])

