#!/usr/bin/env python3

a = []
i = 0
x = 0
s = input()
while s != 'end':
    a.append(int(s))
    s = input()
    i += 1

num = int(input())

while x < len(a):
    a[x] = a[x] + num
    print(a[x])
    x += 1
