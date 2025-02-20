#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file) as f:
    file2 = f.read()
    with open(file2) as f:
        sys.stdout.write(f.read())
