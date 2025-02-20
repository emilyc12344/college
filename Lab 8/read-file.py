#!/usr/bin/env python3

import sys

with open('input.txt') as f:
    s = f.readline()
    while len(s) > 0:
        sys.stdout.write(s)
        s = f.readline()
