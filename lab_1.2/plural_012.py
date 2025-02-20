#!/usr/bin/env python3

import sys

v = ['a', 'e', 'i', 'o', 'u']

for word in sys.stdin:
	word = word.strip()
	l = word[-1]
	sl = word[-2]
	if l == 'h' or l == 'x' or l == 's' or l == 'z':
		print(word + 'es')
	elif l == 'y' and sl not in v:
		print(word[:-1] + 'ies')
	elif l == 'f' or (l == 'e' and sl == 'f'):
		if l == 'e':
			print(word[:-2] + 'ves')
		else:
			print(word[:-1] + 'ves')
	elif l == 'o':
		print(word + 'es')
	else:
		print(word + 's')