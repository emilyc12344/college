#!/usr/bin/env python3

s = str(input())
i = 0

while i < len(s) and s[i] != ' ':
    i += 1

if i < len(s):
    print(i)
else:
    print('-1')
