#!/usr/bin/env python3

import sys

mn = sorted(sys.stdin.readline().split())
s = sys.stdin.readline().strip()

comp = []
for i in range(int(mn[0]), int(mn[1])+1):
    comp.append(i)

for char in s:
    if int(char) in comp:
        comp.remove(int(char))
print(comp[0])
