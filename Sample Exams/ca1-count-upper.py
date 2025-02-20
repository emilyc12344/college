#!/usr/bin/env python3

a = str(input())
tot = 0
i = 0

while i < len(a):
    if (ord(a[i]) != 0) and (64 < ord(a[i]) < 91):
        tot += 1
    i += 1

print(tot)
