#!/usr/bin/env python3

n = int(input())

t = n // 2

if n == 1 or n == 2:
    print('prime')
elif t == 0 or t == 1:
    if (n % 2 != 0) and (n % n == 0) and (n % 1 == 0):
        print('prime')
    else:
        print('not prime')
else:
    if (n % t != 0) and (n % n == 0) and (n % 1 == 0):
        print('prime')
    else:
        print('not prime')
