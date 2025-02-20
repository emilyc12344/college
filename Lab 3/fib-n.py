#!/usr/bin/env python3

n = int(input())
i = 2
t1 = 0
t2 = 1
print(t1)
print(t2)
while i < n:
    curr = t1 + t2
    print(curr)
    t1 = t2
    t2 = curr
    i += 1
