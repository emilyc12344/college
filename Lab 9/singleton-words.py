#!/usr/bin/env python3

import sys

line = sys.stdin.readline().strip()
seen = {}

while len(line) > 0:
    if line not in seen:
        seen[line] = True
    else:
        seen[line] = False
    line = sys.stdin.readline().strip()

for animal in seen:
    if seen[animal]:
        print(animal)
