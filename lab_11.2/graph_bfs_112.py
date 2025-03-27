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

class BFSPaths(object):
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * self.g.V
        self.parent = [-1] * self.g.V
        self.bfs(self.s)

    def bfs(self, s):
        queue = [s]
        self.visited[s] = True
        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    self.parent[w] = v
                    queue.append(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.parent[v]
        path.append(self.s)
        return path[::-1]
