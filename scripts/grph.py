#!/usr/bin/env python3

from Bio import SeqIO

def load_data(filename):
    graph = Graph()
    for record in SeqIO.parse(filename, 'fasta'):
        graph.add_node(Node(name=record.name, data=record.seq))
    return graph


class Node(object):
    def __init__(self, name, ancestors=[], descendents=[], data=None):
        self.name = name
        self.ancestors = ancestors
        self.descendents = descendents
        self.data = data
    
    def add_descendent(self, descendent):
        self.descendents.append(descendent)

    def add_ancestor(self, ancestor):
        self.ancestors.append(ancestor)

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        edge[0].add_descendent(edge[1])
        edge[1].add_ancestor(edge[0])
        self.edges.append(edge)

    def build_overlap_graph(self, k):
        for i, nodei in enumerate(self.nodes):
            for j, nodej in enumerate(self.nodes):
                if nodei.data == nodej.data:
                    continue
                if nodei.data[-k:] == nodej.data[:k]:
                    self.add_edge((nodei, nodej))

    def __repr__(self):
        adjacency_list = ''
        for i, j in self.edges:
            adjacency_list += f'{i.name} {j.name}\n'
        return adjacency_list.strip()


            

if __name__ == '__main__':
    graph = load_data('../data/grph_test.txt')
    graph.build_overlap_graph(3)
    print(graph)

