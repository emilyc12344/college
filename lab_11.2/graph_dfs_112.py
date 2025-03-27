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

class DFSPaths(object):
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * self.g.V
        self.parent = [-1] * self.g.V
        self.dfs(self.s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if self.hasPathTo(v):
            path = [v]
            while path[-1] != self.s:
                path.append(self.parent[path[-1]])
            return path[::-1]
