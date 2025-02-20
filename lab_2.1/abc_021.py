#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
nums = lines[0].split()

a, b, c = 0, 0, 0
n1, n2, n3 = int(nums[0]), int(nums[1]), int(nums[2])

if n1 > n2 and n1 > n3:
	c = n1
	if n2 > n3:
		b = n2
		a = n3
	else:
		b = n3
		a = n2
elif n2 > n1 and n2 > n3:
	c = n2
	if n1 > n3:
		b = n1
		a = n3
	else:
		b = n3
		a = n1
else:
	c = n3
	if n2 > n1:
		b = n2
		a = n1
	else:
		b = n1
		a = n2

let = lines[1].lower()
i = 0
ans = ''

while i < 3:
	if let[i] == 'a':
		ans = ans + str(a) + ' '
	elif let[i] == 'b':
		ans = ans + str(b) + ' '
	else:
		ans = ans + str(c) + ' '
	i += 1

print(ans[:-1])