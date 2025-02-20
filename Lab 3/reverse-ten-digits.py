#!/usr/bin/env python3

n = 10
i = 0
x = 0
f = 0
h = 10

while i < n:
    a = int(input())
    x += a * (10 ** (n - i - 1))
    i += 1
while f < h:
    dig = x % 10
    f += 1
    print(dig)
    x = x // 10
