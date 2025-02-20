#!/usr/bin/env python3

n = 10
i = 0
curr = int(input())
print(curr)

while i < (n - 1):
    num = int(input())
    if curr != num:
        print(num)
    curr = num
    i += 1
