#!/usr/bin/env python3

def reverse_complement(seq):
    revdict = {'A': 'T',
               'C': 'G',
               'G': 'C',
               'T': 'A'}
    revc_seq = [revdict[c] for c in seq][::-1]
    revc_seq = ''.join(revc_seq)
    return revc_seq

if __name__ == '__main__':
    print(reverse_complement('AAAACCCGGT'))

