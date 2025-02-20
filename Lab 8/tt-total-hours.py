#!/usr/bin/env python3

s = input()
tot = 0
while s != 'end':
    a = s.split()
    tot += int(a[2])
    s = input()

print(tot)
