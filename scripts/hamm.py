#!/usr/bin/env python3

def hamming(seq1, seq2):
    nbases = len(seq1)
    assert nbases == len(seq2)

    hdist = 0
    for i in range(nbases):
        if seq1[i] != seq2[i]:
            hdist += 1
    return hdist

if __name__ == '__main__':
    with open('../data/hamm_test.txt') as infile:
        seq1 = infile.readline().strip()
        seq2 = infile.readline().strip()
        print(hamming(seq1, seq2))

