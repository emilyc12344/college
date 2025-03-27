#!/usr/bin/env python3

import sys

class Graph(object):
    
    def __init__(self, V):
        self.adj = {}
        self.V = V
        self.degs = {}
        for v in range(V):
            self.adj[v] = []
        for v in range(V):
            self.degs[v] = 0

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.degs[v] += 1
        self.degs[w] += 1

    def degree(self, v):
        return self.degs[v]

    def maxDegree(self):
        return max(self.degs.values())

    def avgDegree(self):
        return sum(self.degs.values()) / len(self.degs.values())

def main():

    V = int(sys.stdin.readline().strip())

    g = Graph(V)

    for line in sys.stdin:
        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

    for v in range(g.V):
        print('Vertex {} connects to {}'.format(v, g.adj[v]))

    for v in range(V):
        print('Degree of vertex {} is {}'.format(v, g.degree(v)))
    print('Maximum degree is {}'.format(g.maxDegree()))
    print('Average degree is {:.2f}'.format(g.avgDegree()))
if __name__ == '__main__':
    main()
