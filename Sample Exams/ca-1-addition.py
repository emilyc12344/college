#!/usr/bin/env python3

n = input() + ' '
i = 0
x = 0
s = 0
c = 0
a = True
b = True
tot = 0

while i < len(n):
    if n[i] == ' ':
        s = i
        c += 1
    if c == 1 and a:
        num1 = n[x:s]
        a = False
        x = s + 1
    if c == 2 and b:
        num2 = n[x:s]
        b = False
        x = s + 1
    if c == 3:
        num3 = n[x:]
    i += 1

print(int(num1) + int(num2) + int(num3))
