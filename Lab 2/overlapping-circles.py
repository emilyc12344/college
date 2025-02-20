#!/usr/bin/env python3

x = int(input())
y = int(input())
r = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

dis = (((x2 - x) ** 2) + ((y2 - y) ** 2)) ** 0.5

if dis >= (r + r2):
    print('no')
else:
    print('yes')
