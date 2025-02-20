#!/usr/bin/env python3

import sys

seen = {}

with open('a.txt') as f:
    lines = f.readlines()

    i = 0
    while i < len(lines):
        seen[lines[i].strip()] = 0
        i += 1
with open('b.txt') as f:
    lines = f.readlines()

    i = 0
    while i < len(lines):
        seen[lines[i].strip()] = 0
        i += 1

i = 0
keys = list(seen.keys())
while i < len(keys):
    print(keys[i])
    i += 1
