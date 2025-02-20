#!/usr/bin/env python3

n = int(input())
i = 0

# n[0] == n[1]
while i < n:
    num = str(input())
    if num[0] == num[1]:
        print(num)
    i += 1
