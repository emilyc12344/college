#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()

for n in nums:
	l = [i for i in range(2, int(n) + 1)]
	prime = []
	for n in l:
		check = 0
		for i in range(2, int(n)):
			if n % i != 0:
				check += 1
		if check == len(range(2, int(n))):
			prime.append(n)
	print('Primes:',prime)