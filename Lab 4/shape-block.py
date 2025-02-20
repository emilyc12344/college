#!/usr/bin/env python3

n = int(input())
i = 0

print('*' * n)

while i < (n - 2):
    print('*' + ('-' * (2)) + '*')
    i += 1

print('*' * n)
