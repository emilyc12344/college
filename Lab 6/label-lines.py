#!/usr/bin/env python3

a = []
i = 0
x = 0
s = input()

while s != 'end':
    a.append(s)
    s = input()
    i += 1

while x < len(a):
    print(x, len(a), a[x])
    x += 1
