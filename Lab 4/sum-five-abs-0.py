#!/usr/bin/env python3

num = int(input())
tot = ((num ** 2) ** 0.5)

while num != 0:
    num = int(input())
    tot = int(tot + ((num ** 2) ** 0.5))

print(tot)
