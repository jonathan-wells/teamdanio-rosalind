#!/usr/bin/env python3

def hamming(seq1, seq2):
    """Return the Hamming distance between two strings."""
    nbases = len(seq1)
    # Here we just want to check if seqs are same length. If not, assert will
    # fail and the program aborts
    assert nbases == len(seq2)

    hdist = 0
    for i in range(nbases):
        if seq1[i] != seq2[i]:
            hdist += 1
    return hdist

if __name__ == '__main__':
    # This little snippet just reads the two lines from the input data
    with open('../data/hamm_test.txt') as infile:
        # Each readline reads exactly one line, and then moves to next.
        seq1 = infile.readline().strip()
        seq2 = infile.readline().strip()
        print(hamming(seq1, seq2))

