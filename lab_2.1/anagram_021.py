#!/usr/bin/env python3

import sys

for lines in sys.stdin:
	x, y = lines.lower().split()
	print(sorted(x) == sorted(y))