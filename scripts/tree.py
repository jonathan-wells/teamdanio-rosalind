#!/usr/bin/env python3

import grph

def load_data(filename):
    graph = grph.Graph()
    e = 0
    with open(filename) as infile:
        k = int(infile.readline())
        for i in range(1, k+1):
            graph.add_node(grph.Node(name=str(i)))
        for line in infile:
            if len(line) > 1:
                e += 1
    print(k - 1 - e)
    print(k, e)
            
if __name__ == '__main__':
    load_data('../data/rosalind_tree.txt')
