#!/usr/bin/env python3

n = str(input())
i = 0
tot = 0

while i < len(n):
    p = (len(n) - 1) - i
    if int(n[i]) > 0:
        tot = tot + (2 ** p)
    i += 1

print(tot)
