'''
My solution to Rosalind Bioinformatics Problem
Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

import sys
import os

def Transcribed(fi):
    '''
    :return: The transcribed RNA string.
    '''
    ipt_file = open(fi, 'r').read()
    print ipt_file.replace('T','U')
    output_name = 'output_'+fi
    with open(output_name, 'a') as f:
        f.write(ipt_file.replace('T','U'))
Transcribed(sys.argv[1])
