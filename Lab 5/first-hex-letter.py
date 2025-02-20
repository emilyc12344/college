#!/usr/bin/env python3

n = int(input())
opt = '0123456789abcdef'
tot = ''
a = 0
i = 0
x = 0
b = True

while b:
    a = n / (16 ** i)
    if a < 1:
        p = i - 1
        b = False
    i += 1

while p >= 0:
    v = n // (16 ** p)
    n = n % (16 ** p)
    p -= 1
    tot = tot + opt[v]

b = True
while x < len(tot) and b:
    if 'a' <= tot[x] <= 'f':
        print(tot[x])
        b = False
    x += 1
