#!/usr/bin/env python3

n = int(input())

if n % 10 == 1:
    n = str(n) + 'st'
elif n % 10 == 2:
    n = str(n) + 'nd'
elif n % 10 == 3:
    n = str(n) + 'rd'
else:
    n = str(n) + 'th'

print(n)
