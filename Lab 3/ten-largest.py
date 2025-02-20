#!/usr/bin/env python3

n = 10
i = 0
big = int(input())

while i < (n - 1):
    curr = int(input())
    if curr > big:
        big = curr
    i += 1
print(big)
