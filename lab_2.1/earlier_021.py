#!/usr/bin/env python3

import sys

for time in sys.stdin:
	time = time.split(':')
	hour = int(time[0])
	m = int(time[1])

	if (m - 47 >= 0):
		m = m - 47
	else:
		rem = 47 - m
		m = 60 - rem
		if hour > 0:
			hour = hour - 1
		else:
			hour = 23
	print(f'{hour:0>2}:{m:0>2}')