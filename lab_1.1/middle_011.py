#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	if len(line) % 2 != 0:
		mid = (len(line) // 2)
		print(line[mid:mid + 1])
	else:
		print('No middle character!')