'''
My solution to Rosalind Bioinformatics Problem
Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb/
'''

import sys
import itertools

# A mendel distribution 
def mendel(fi):

    m, n, k = open(fi, 'r').readline().split(' ')
    Dom = 'AA'
    Het = 'Aa'
    Rec = 'aa'
    L = [Dom]*int(m)
    L.extend([Het]*int(n))
    L.extend([Rec] * int(k))
    permutation = list(itertools.permutations(L, 2))
    res = []
    for per in permutation:
        for letter in per[0]:
            for let in per[1]:
                res.append(letter + let)
    unique = list(set(res))
    freq_dom = res.count('AA')
    freq_het = res.count('Aa') + res.count('aA')
    freq_rec = res.count('aa')

    all_freq = [freq_dom, freq_het, freq_rec]

    # Probability at least one dominant allele
    Pdom = (freq_dom+freq_het) / float(sum(all_freq))
    print Pdom

    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(str(Pdom))

mendel(sys.argv[1])
