#!/usr/bin/env python3

import sys

f1 = sys.argv[1]

with open(f1) as f:
    f2 = f.readline()

with open(f2) as f:
    sys.stdout.write(f.read())
