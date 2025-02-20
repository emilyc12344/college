#!/usr/bin/env python3

import sys

file = sys.argv[1]
contacts = {}
i = 0

with open(file) as f:
    lines = f.readlines()
    while i < len(lines):
        l = lines[i].split()
        name = l[0]
        if name not in contacts:
            contacts[name] = l[1].strip()
        i += 1

for l in sys.stdin:
    l = l.strip()
    print(f'Name: {l}')
    if l in contacts:
        print(f'Phone: {contacts[l]}')
    else:
        print('No such contact')
