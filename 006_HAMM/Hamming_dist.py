'''
My solution to Rosalind Bioinformatics Problem
Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
'''

import sys
def out_mutation(seqA,seqB, ss):
    for x in xrange(0, len(seqA), 100):
        print 'Sequence A', seqA[x:x+100]
        print '          ', ss[x:x+100]
        print 'Sequence B', seqB[x:x+100]

def Hamming_distance(fi):
    seqs = open(fi, 'r').read().split('\n')
    seq_a = seqs[0]
    seq_b = seqs[1]
    mutA = ''
    mutB = ''
    dist = 0
    ss = ''
    for x in xrange(0, len(seq_a)):
        if seq_a[x] == seq_b[x]:
            mutA += seq_a[x]
            mutB += seq_b[x]
            ss += ' '
        if seq_a[x] != seq_b[x]:
            mutA += seq_a[x].lower()
            mutB += seq_b[x].lower()
            ss += '|'
            dist +=1
    out_mutation(mutA, mutB, ss)
    print dist
    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(str(dist))


Hamming_distance(sys.argv[1])
