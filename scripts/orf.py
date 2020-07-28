#!/usr/bin/env python3

from Bio import SeqIO
from rna import transcribe
from revc import reverse_complement
from prot import load_codons

def extract_subseqs(orfs):
    subseqs = []
    for seq in orfs:
        for i, aa in enumerate(seq):
            if aa == 'M':
                subseqs.append(seq[i:])
    return set(subseqs)

def find_orfs(seq):
    """Find all potential open reading frames in a sequence."""
    frames = []
    for i in range(3):
        frames.append(transcribe(seq[i:]))
        frames.append(transcribe(reverse_complement(seq)[i:]))
    
    orfs = set()
    codons = load_codons()
    for frame in frames:
        i = 0
        recording = False 
        current_orf = ''
        
        while True:
            codon = frame[i:i+3]
            aa = codons.get(codon, 'Stop')
            
            if len(codon) != 3:
                break  # Because reached end of frame
            
            if codon == 'AUG':
                recording = True
            if aa != 'Stop' and recording:
                current_orf += aa
            elif aa == 'Stop':
                recording = False
                orfs.add(current_orf)
                current_orf = ''
            i += 3

    orfs.remove('')
    orfs = extract_subseqs(orfs)

    return orfs


if __name__ == '__main__':
    for record in SeqIO.parse('../data/rosalind_orf.txt', 'fasta'):
        seq = str(record.seq)
        orfs = find_orfs(seq)
        for o in orfs:
            print(o)
