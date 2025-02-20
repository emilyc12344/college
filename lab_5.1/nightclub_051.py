#!/usr/bin/env python3

import sys

line = sys.stdin.readlines()

max = int(line[0].strip())
rn = 0
den = 0

line = line[1:]
for curr in line:
    curr = curr.strip().split()
    #print(curr, rn, den, max)
    if curr[0] == 'enter' and (rn + int(curr[1])) < max:
        rn += int(curr[1])
    elif curr[0] == 'leave':
        rn -= int(curr[1])
    else:
        den += 1

print(den)
