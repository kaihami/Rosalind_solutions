'''
My solution to Rosalind Bioinformatics Problem
Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot/
'''

import sys
from collections import defaultdict

S = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''.split()

gen = defaultdict(list)
for x in xrange(0, len(S),2):
    if S[x+1] in gen.keys():
        gen[S[x+1]].append(S[x])
    if S[x+1] not in gen.keys():
        gen[S[x + 1]] = [S[x]]

def translate(fi, gen):
    # Translate a mRNA seq in protein, frame 1
    seq = open(fi, 'r').readline()
    protein = ''
    for x in xrange(0, len(seq),3):
        #seq[x:x+3]
        for k,v in gen.items():
            if seq[x:x+3] in v:
                if k != 'Stop':
                    protein += k

                break
        if k == 'Stop':
            break
    print protein
    output_name = 'output_'+fi

    with open(output_name, 'a') as f:
        f.write(str(protein))

translate(sys.argv[1], gen)
