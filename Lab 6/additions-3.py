#!/usr/bin/env python3

n1 = 0
n2 = 0
n = 10
i = 0
x = 0
tot = 0
s = input()
while tot != 1000:
    x = 0
    while x < len(s):
        if s[x] == '+':
            num1 = int(s[:x])
            num2 = int(s[x:])
        x += 1
    tot = num1 + num2
    print(tot)
    if tot != 1000:
        s = input()
    i += 1
