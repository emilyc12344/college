#!/usr/bin/env python3

n1 = 0
n2 = 0
n = 10
i = 0
x = 0
s = input()
while i < n:
    x = 0
    while x < len(s):
        if s[x] == '+':
            num1 = int(s[:x])
            num2 = int(s[x:])
        x += 1
    print(num1 + num2)
    if i < (n - 1):
        s = input()
    i += 1
