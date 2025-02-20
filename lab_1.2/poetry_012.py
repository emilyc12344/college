#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
#print(lines)
c_l = 0

for l in lines:
	l = l.strip()
	if len(l) > c_l:
		c_l = len(l) 

for i in lines:
	i = i.strip()
	print(f'{i:^{c_l}s}')