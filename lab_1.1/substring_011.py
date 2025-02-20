#!/usr/bin/env python3

import sys

for lines in sys.stdin:
	l = lines.split()
	l[0] = l[0].lower()
	l[1] = l[1].lower()
	print(l[0] in l[1])