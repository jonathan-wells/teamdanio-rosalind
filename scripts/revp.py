#!/usr/bin/env python3

import revc
from Bio import SeqIO

def is_reverse_palindrome(seq):
    if len(seq) == 0:
        return True
    elif len(seq) == 1:
        return False
    elif seq[0] == revc.reverse_complement(seq[-1]):
        return is_reverse_palindrome(seq[1:-1])
    else:
        return False

def enumerate_palindromes(seq, minlen, maxlen):
    n = len(seq)
    for i in range(n):
        for j in range(i+minlen, n+1):
            substring = seq[i:j]
            if is_reverse_palindrome(substring) and len(substring) <= maxlen:
                print(i+1, len(substring))

if __name__ == '__main__':
    for record in SeqIO.parse('../data/rosalind_revp.txt', 'fasta'):
        seq = str(record.seq)
        enumerate_palindromes(seq, 4, 12)
        
