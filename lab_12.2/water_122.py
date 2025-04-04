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

for curr in houses:
    if curr in list(h.keys()):
        for i in h[curr]:
            if curr in has_water or curr in no_water:
                pass
            elif i in has_water:
                has_water.append(curr)
            else:
                no_water.append(curr)
    else:
        no_water.append(curr)

print(no_water)
