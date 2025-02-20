#!/usr/bin/env python3

import sys

seen = {}

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
            print(lines[i].strip())
        i += 1
