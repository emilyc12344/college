#!/usr/bin/env python3

import sys

for lines in sys.stdin:
	i = 0
	tot = 0
	l = lines.split()
	l[0] = l[0].lower()
	l[1] = l[1].lower()
	while i < len(l[0]):
		if l[0][i] in l[1]:
			tot += 1
			index = l[1].index(l[0][i])
			l[1] = l[1][:index] + l[1][index + 1:]
		i += 1
	print(tot == len(l[0]))