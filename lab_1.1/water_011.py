#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

tot = int(lines[0])
b_f = 0
buckets = lines[1].split()

i = 0
while i < len(buckets) and tot >= 0:
	#print(tot)
	tot = tot - int(buckets[i])
	b_f += 1
	i += 1

if i == len(buckets) and tot >= 0:
	print(b_f)
else:
	print(b_f - 1)