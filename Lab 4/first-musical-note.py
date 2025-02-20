#!/usr/bin/env python3

s = str(input())
i = 0
a = True

while a:
    if 'a' <= s[i] <= 'g':
        print(s[i])
        a = False
    i += 1
