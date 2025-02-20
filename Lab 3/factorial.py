#!/usr/bin/env python3

n = int(input())
i = 0
tot = 1

while i < n:
    tot *= (i + 1)
    i += 1

print(tot)
