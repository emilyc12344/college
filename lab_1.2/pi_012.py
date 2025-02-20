#!/usr/bin/env python3

import sys, math

for n in sys.stdin:
	n = int(n.strip())
	print(f'{math.pi:.{n:d}f}')