#!/usr/bin/env python3

f = 0
n = int(input())
x = n
h = len(str(n))
rev_num = 0

while f < h:
    dig = n % 10
    f += 1
    n = n // 10
    rev_num += dig * (10 ** (h - f))

if rev_num == x:
    print('yes')
else:
    print('no')
