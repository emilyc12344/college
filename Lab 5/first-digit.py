#!/usr/bin/env python3

s = str(input())
i = 0
a = True

while a and i < len(s):
    if (ord('0') - 1) < ord(s[i]) and ord(s[i]) < (ord('9') + 1):
        print(s[i], i)
        a = False
    i += 1
