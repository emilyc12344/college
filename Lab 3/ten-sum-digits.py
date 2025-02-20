#!/usr/bin/env python3

n = 10
i = 0
tot = 0

while i < n:
    a = int(input())
    if a < 0:
        a *= -1
    a %= 10
    tot += a
    i += 1

print(tot)
