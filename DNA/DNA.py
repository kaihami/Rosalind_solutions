'''
My solution to Rosalind Bioinformatics Problem
Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
'''

import sys

def Count_frequency_nucleotide(fi):
    '''
    :return: Frequency of 'A', 'C', 'G', 'T'.
             Space separated
    '''
    ipt_file = open(fi, 'r').read()
    dna = 'A C G T'.split()
    freq_list = [str(ipt_file.count(letter)) for letter in dna]
    for letter, freq in zip(dna, freq_list):
        print '%s: %s' % (letter, freq)
        print '*'*20
    output_name = 'output_'+fi
    with open(output_name, 'a') as f:
        f. write(' '.join(freq_list))

Count_frequency_nucleotide(sys.argv[1])
