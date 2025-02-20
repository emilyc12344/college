#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().lower()
    if line[0] == 'h' and line[-1] == 'y':
        es = len(line) - 2
        print('h' + ('e' * (es + es)) + 'y')
