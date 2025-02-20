#!/usr/bin/env python3

import sys

for line in sys.stdin:
	if line[0] == 'm':
		print('M' + line[1:-1])
	elif ' m' in line:
		ind = line.index(' m')
		print(line[:ind] + ' M' + line[ind + 2:-1])
	else:
		print(line.strip())
