#!/usr/bin/env python3

i = 0
n = 10
tot = 0

while i < n:
    a = int(input())
    if a > 0:
        tot += a
    i += 1

print(tot)
