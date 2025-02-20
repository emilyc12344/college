#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()

for n in nums:
	l = [i for i in range(1, int(n) + 1)]
	m_3 = [i for i in l if i % 3 == 0]
	m_3_s = [i * i for i in l if i % 3 == 0]
	m_4_d = [i * 2 for i in l if i % 4 == 0]
	m_3_or_4 = [i for i in l if i % 3 == 0 or i % 4 == 0]
	m_3_and_4 = [i for i in l if i % 3 == 0 and i % 4 == 0]
	print(f'Multiples of 3: {m_3}\nMultiples of 3 squared: {m_3_s}\nMultiples of 4 doubled: {m_4_d}\nMultiples of 3 or 4: {m_3_or_4}\nMultiples of 3 and 4: {m_3_and_4}')
