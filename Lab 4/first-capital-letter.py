#!/usr/bin/env python3

s = str(input())
i = 0
a = True

while i < len(s) and a:
    if 64 < ord(s[i]) < 91:
        print(i)
        a = False
    i += 1
