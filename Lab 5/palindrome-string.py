#!/usr/bin/env python3

s = str(input())
r_s = ''
i = 0
x = -1

while i < len(s):
    r_s = r_s + s[x]
    x -= 1
    i += 1

if r_s == s:
    print('palindrome')
