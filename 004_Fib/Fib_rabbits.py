'''
My solution to Rosalind Bioinformatics Problem
Title: Rabbits and Recurrence Relations
Rosalind ID: Fib
Rosalind #: 004
URL: http://rosalind.info/problems/fib/
'''

import sys

# A memoization solution for n, k rabbits problem
# Fast solution, uses more memory
def fib(n,k):
    '''
    :param n: number of months
    :param k: each pair of rabbits produces k-litters
    :return: number of rabbits.
    '''
    def fib_memo(n,k,cache):
        if n in cache:
            return cache[n]
        answer = fib_memo(n - 1, k,cache) + (fib_memo(n - 2,k, cache)*k)
        cache[n] = answer
        return answer
    cache = {1: 1, 2: 1}
    return fib_memo(n,k, cache)

def Wrap(fi):

    n, k = [int(x) for x in open(fi, 'r').read().replace('\n', ''). split(' ')]

    output_name = 'output_'+fi
    print 'Total number of Rabbits:', str(fib(n,k))
    with open(output_name, 'a') as f:
        f.write(str(fib(n,k)))

Wrap(sys.argv[1])
