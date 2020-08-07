#!/usr/bin/env python3

import prot
from Bio import SeqIO

def splice(seq, introns):
    """Removes introns from a given sequence."""
    for i in introns:
        seq = seq.replace(i, '')
    return seq

def load_data(filename):
    """Returns sequence and introns

    Expects to receive data in fasta format, with first entry the unspliced
    sequence, and subsequent entries the introns to be removed.
    """
    data = [str(record.seq) for record in SeqIO.parse(filename, 'fasta')]
    seq, introns = data[0], data[1:]
    return seq, introns

if __name__ == '__main__':
    seq, introns = load_data('../data/rosalind_splc.txt')
    spliced_seq = splice(seq, introns)
    # Note that we also transcribe the sequence here.
    protein = prot.translate(spliced_seq.replace('T', 'U'))
    print(protein)
