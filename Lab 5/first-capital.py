#!/usr/bin/env python3

s = str(input())
i = 0
a = True

while i < len(s) and a:
    if (ord('A') - 1) < ord(s[i]) and ord(s[i]) < (ord('Z') + 1):
        print(s[i], i)
        a = False
    i += 1
