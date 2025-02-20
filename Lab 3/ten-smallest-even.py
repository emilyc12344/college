#!/usr/bin/env python3

n = 10
i = 0
small = int(input())

while i < (n - 1):
    curr = int(input())
    if curr < small and curr % 2 == 0:
        small = curr
    i += 1
print(small)
