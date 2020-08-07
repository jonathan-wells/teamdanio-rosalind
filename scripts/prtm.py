#!/usr/bin/env python3

# Create a dictionary for the mol. mass of amino acids.
with open('../data/monoisotopic_mass_table.txt') as infile:
    mim = {i.split()[0]: float(i.split()[1]) for i in infile}

# Iterate through protein sequence and add masses.
mass = 0.0
with open('../data/rosalind_prtm.txt') as infile:
    proteinseq = infile.readline().strip()
    for aa in proteinseq:
        try:
            mass += mim[aa]
        except KeyError:
            raise KeyError(f'{aa} is not an amino acid')
    print(f'{mass:.3f}')
