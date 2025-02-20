#!/usr/bin/env python3

n = 10
i = 0
small = int(input())

while i < (n - 1):
    curr = int(input())
    if curr < small:
        small = curr
    i += 1
print(small)
