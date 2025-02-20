#!/usr/bin/env python3

import sys

v = 'aeiouAEIOU'
i = 0
tot = 0
s = sys.stdin.read()

while i < len(s):
    if s[i] in v:
        tot += 1
    i += 1

print(tot)
