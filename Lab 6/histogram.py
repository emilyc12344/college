#!/usr/bin/env python3

i = 0
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = input()
while n != 'end':
    n = int(n)
    a[n] += 1
    n = input()

while i < len(a):
    print(i, '*' * a[i])
    i += 1
