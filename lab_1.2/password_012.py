#!/usr/bin/env python3

import sys

for p in sys.stdin:
	n = 0
	l = 0
	u = 0
	s = 0
	p = p.strip()
	for i in p:
		#print(i)
		if i.isnumeric():
			n = 1
		elif i.islower():
			l = 1
		elif i.isupper():
			u = 1
		else:
			s = 1
	print(n + l + u + s)