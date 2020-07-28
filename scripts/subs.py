#!/usr/bin/env python3

def load_data():
    with open('../data/rosalind_subs.txt') as infile:
        s = infile.readline().strip()
        t = infile.readline().strip()
    return t, s

def find_substring(t, s):
    q, r = len(t), len(s)
    for i in range(r):
        if t == s[i:i+q]:
            yield i+1

if __name__ == '__main__':
    t, s = load_data()
    locs = [str(i) for i in find_substring(t, s)]
    print(' '.join(locs))

