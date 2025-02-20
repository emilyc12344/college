#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	line = line[1:-1]
	if line:
		print(line)
