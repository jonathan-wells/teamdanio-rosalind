#!/usr/bin/env python3

import re

def load_codons():
    codons = {}
    with open('../data/codon_table.txt') as infile:
        for line in infile:
            tokens = re.findall(r'[UCGA]{3}\s+\w+', line)
            for tok in tokens:
                codon, residue = tok.split()
                codons[codon] = residue
    return codons

def translate_string(rnastring):
    codons = load_codons()
    protstring = ''
    for i in range(0, len(rnastring), 3):
        codon = codons[rnastring[i:i+3]]
        if codon == 'Stop':
            return protstring
        protstring += codons[rnastring[i:i+3]]
    return protstring

if __name__ == '__main__':
    with open('../data/rosalind_prot.txt') as infile:
        rnastring = infile.readline().strip()
    print(translate_string(rnastring))
