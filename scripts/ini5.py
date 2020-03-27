#!/usr/bin/env python3

def get_lines(filename):
    """Returns list of lines from file, with trailing whitespace removed."""
    lines = []
    with open(filename) as infile:
        for line in infile:
            # Add lines with removed newline
            lines.append(line.strip())
    return lines

def get_lines_v2(filename):
    """Same function as above but less verbose."""
    with open(filename) as infile:
        # This pattern is known as a 'list comprehension'
        lines = [line.strip() for line in infile]
    return lines

def print_even_lines(lines):
    """Does what it says on the tin. Doesn't return anything, just prints.'"""
    for i, line in enumerate(lines, 1):
        if i % 2 == 0:
            print(line)

def print_even_lines_v2(lines):
    """Same as above, but without using the enumerate function."""
    i = 1
    for line in lines:
        if i % 2 == 0:
            print(line)
        i += 1

lines = get_lines('../data/ini5_test.txt')
print_even_lines(lines)
