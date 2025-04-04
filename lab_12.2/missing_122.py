#!/usr/bin/env python3

import sys

mn = sys.stdin.readline().split()
mn = sorted([int(mn[0]), int(mn[1])])
s = sys.stdin.readline().strip()
comp = []
for i in range(int(mn[0]), int(mn[1])+1):
    comp.append(i)
for curr in comp:
    if mn[1] == 10000:
        print(1001)
        break
    elif str(curr) in s:
        s = s[len(str(curr)):]
    else:
        print(curr)
        break

