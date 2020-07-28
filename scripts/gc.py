#!/usr/bin/env python3

from Bio import SeqIO

def load_fasta(filename):
    return list(SeqIO.parse(filename, 'fasta'))

def calc_gc(seq):
    gccount = len([i for i in seq if i == 'G' or i == 'C'])
    return gccount/len(seq)

def get_max_gc(seqrecords):
    currmax_gc = 0
    currmax_id = ''
    for record in seqrecords:
        gc = calc_gc(record.seq)
        if gc > currmax_gc:
            currmax_gc = gc
            currmax_id = record.id
    return currmax_id, currmax_gc*100

if __name__ == '__main__':
    seqrecords = load_fasta('../data/rosalind_gc.txt')
    seqid, gcval = get_max_gc(seqrecords)
    print(seqid)
    print(f'{gcval:.6f}')
