#!/usr/bin/env python3

import sys

for lines in sys.stdin:
	lines = lines.lower()
	r_line = ''
	line = ''
	i = -1
	while i * -1 < len(lines) + 1:
		if lines[i].isalnum():
			r_line = r_line + lines[i]
		i -= 1
	i = 0
	while i < len(lines):
		if lines[i].isalnum():
			line = line + lines[i]
		i += 1
	
	print(r_line == line)