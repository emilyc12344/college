#!/usr/bin/env python3

n = int(input())
i = 2
x = -1
print(0)
print(-1)
while i < n:
    x = int((((x ** 2) ** 0.5) + 1) * ((x // ((x ** 2) ** 0.5)) * (-1)))
    print(x)
    i += 1
