#!/usr/bin/env python3

# This script is overkill for such a simple job. You would not normally write a
# function whose sole purpose is to replace a letter in a string.

def transcribe(rna_seq):
    return rna_seq.replace('T', 'U')

def read_seq(filename):
    return open(filename).readline().strip()

if __name__ == '__main__':
    rna_seq = read_seq('../data/rna_test.txt')
    dna_seq = transcribe(rna_seq)
    print(dna_seq)

