#!/usr/bin/env python3

a = []
i = 0
x = 0
n = input()
while n != 'end':
    a.append(n)
    n = input()

while i < len(a):
    x = (i + 1) * -1
    print(a[x])
    i += 1
