#!/usr/bin/env python3

import sys

for line in sys.stdin:
    valid = []
    dupe = []
    line = line.strip().split()
    for n in line:
        n = int(n)
        if n in valid:
            valid.pop(valid.index(n))
            dupe.append(n)
        elif n not in dupe:
            valid.append(n)
    if len(valid) > 0:
        print(sorted(valid)[-1])
    else:
        print('none')
