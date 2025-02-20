#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()

for n in nums:
	l = [i for i in range(1, int(n) + 1)]
	nums = [i if i % 3 == 0 else 0 for i in l]
	print(f'Non-multiples of 3 replaced: {nums}')