#!/usr/bin/env python3

n = str(input())
tot = 0
i = 0

while i < len(n):
    tot += int(n[i])
    i += 1

print(tot)
