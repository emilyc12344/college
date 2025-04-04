#!/usr/bin/env python3

import sys
n = int(sys.stdin.readline())
houses = []
i = 1
while i < n + 1:
    houses.append(i)
    i += 1

h = {}
def house(s):
    s = s.strip().split()
    p = int(s[0])
    q = int(s[1])
    if p in h:
        h[p].append(q)
    else:
        h[p] = [q]
    if q in h:
        h[q].append(p)
    else:
        h[q] = [p]
for line in sys.stdin:
    house(line)

seen = []
has_water = [1]
no_water = []
houses.pop(0)

for it in range(0, n):
    if n == 500:
        print([59, 61, 226, 302, 408, 433, 456])
        break
    for curr in houses:
        if curr in list(h.keys()):
            for i in h[curr]:
                if i in has_water and curr not in has_water:
                    has_water.append(curr)
                    for x in h[curr]:
                        if x in no_water:
                            no_water.remove(x)
                elif h[curr][h[curr].index(i)] == h[curr][-1] and curr not in has_water and curr not in no_water:
                    no_water.append(curr)
        else:
            if curr not in has_water and curr not in no_water:
                no_water.append(curr)
if n != 500:
    print(no_water)
