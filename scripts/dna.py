#!/usr/bin/env python3

from collections import defaultdict, Counter

def read_string(filename):
    """Return dna sequence string from file."""
    with open(filename) as infile:
        dna_seq = infile.readline()
        dna_seq = dna_seq.strip()
    return dna_seq

def freq_count(dna_seq):
    """Return dictionary of base frequencies."""
    freq_dict = defaultdict(int)
    for base in dna_seq:
        freq_dict[base] += 1
    return freq_dict

def print_freqs(freq_dict):
    bases = ['A', 'C', 'T', 'G']
    freqs = []
    for key in bases:
        # Convert "int" type to "str" type first
        freq_string = str(freq_dict[key])
        freqs.append(freq_string)
        pretty_string = ' '.join(freqs)  # Otherwise this wont work.

def print_freqs_v2(freq_dict):
    """This is the way Nathalie suggested - its better"""
    for base in sorted(freq_dict):
        # By default the print function ends each line with a newline character
        # (i.e. '\n'). You can change this by explicitly setting it to something
        # different. For example a space character, as we've done here, or
        # commas, or whatever you like.
        print(freq_dict[base], end=' ')
    print()  # After this for loop will will just print an empty line.

if __name__ == '__main__':
    s = read_string('../data/dna_test.txt')
    fd = freq_count(s)
    print_freqs_v2(fd)

