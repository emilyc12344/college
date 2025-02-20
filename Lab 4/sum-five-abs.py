#!/usr/bin/env python3

n = 5
i = 0
tot = 0

while i < n:
    num = int(input())
    tot = int(tot + ((num ** 2) ** 0.5))
    i += 1

print(tot)
