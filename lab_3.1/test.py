#!/usr/bin/env python3

import sys

l = [(2 ** 127) - 1]
for n in l:
	check = 0
	for i in range(2, int(n)):
		if n % i != 0:
			check += 1
	if check == len(range(2, int(n))):
		prime.append(n)
	else:
	    print('Faker', n)
print('Primes:',prime)
