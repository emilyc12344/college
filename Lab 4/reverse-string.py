#!/usr/bin/env python3

s = str(input())
rev = ''
i = 0

while i < len(s):
    rev += s[-1 - i]
    i += 1

print(rev)
