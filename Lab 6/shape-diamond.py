#!/usr/bin/env python3

import sys

n = int(input())
h_n = (n // 2) - 1
i = 0
y = n - (n - 1)

while i < n:
    if i == (n // 2):
        print('*' * n)
        y -= 2
        h_n += 1
    elif i < (n // 2):
        print(' ' * (h_n), '*' * (y))
        h_n -= 1
        y += 2
    else:
        print(' ' * (h_n), '*' * (y))
        h_n += 1
        y -= 2
    i += 1
