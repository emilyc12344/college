#!/usr/bin/env python3

s = input()
while s != 'end':
    a = s.split()
    if int(a[2]) > 1:
        print(s)
    s = input()
