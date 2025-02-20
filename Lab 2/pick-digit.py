#!/usr/bin/env python3

n = str(input())
p = int(input())
num = []
x = -1

while len(num) < len(n):
    num.append(n[x])
    x -= 1

print(num[p])
