#!/usr/bin/env python3

n = str(input())
a = True

while n != 'end':
    i = 1
    isAlpha = True
    while i < len(n):
        if n[i] < n[i - 1]:
            isAlpha = False
        i += 1
    if isAlpha:
        print(n)
    n = str(input())
