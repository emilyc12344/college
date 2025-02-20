#!/usr/bin/env python3

import sys

for email in sys.stdin:
	nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	names = email.split('.')[:2]
	names[1] = names[1][:names[1].index('@')]
	i = 0
	while (i * -1) < len(names[1]):
		i -= 1
		#print(i, names[1][i])
		if names[1][i] in nums:
			names[1] = names[1][:i]
			i = 0
	names[0] = names[0].capitalize()
	names[1] = names[1].capitalize()
	print(names[0] + ' ' + names[1])