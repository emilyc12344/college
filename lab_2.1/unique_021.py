#!/usr/bin/python3

import string
import sys

seen = []

for s in sys.stdin:
	line = ''.join(ch for ch in s if ch not in string.punctuation)
	lines = line.lower().split()
	i = 0
	while i < len(lines):
		if lines[i] not in seen:
			seen.append(lines[i])
		i += 1

print(len(seen))
