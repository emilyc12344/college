#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r = int(input())

x2 = int(input())
y2 = int(input())

a = (x2 - x1) * (x2 - x1)
b = (y2 - y1) * (y2 - y1)
dis = (a + b) ** 0.5

if dis < r:
    print('yes')
else:
    print('no')
