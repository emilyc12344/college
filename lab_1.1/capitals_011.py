#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	mid = line[1:-1]
	print((line[0].capitalize()) + mid + (line[-1].capitalize()))
