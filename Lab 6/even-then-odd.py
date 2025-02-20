#!/usr/bin/env python3

i = 0
x = 0
a = []
n = input()
while n != 'end':
    n = int(n)
    if n % 2 == 0:
        print(n)
    else:
        a.append(n)
    n = input()

while x < len(a):
    print(a[x])
    x += 1
