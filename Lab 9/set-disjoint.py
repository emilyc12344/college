#!/usr/bin/env python3

import sys

seen = {}
match = 0
with open('a.txt') as f:
    lines = f.readlines()

    i = 0
    while i < len(lines):
        seen[lines[i].strip()] = True
        i += 1

with open('b.txt') as f:
    lines = f.readlines()

    i = 0
    while i < len(lines):
        if lines[i].strip() in seen:
            match += 1
        i += 1

if match >= 1:
    print('intersecting')
else:
    print('disjoint')
