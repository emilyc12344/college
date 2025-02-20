#!/usr/bin/env python3

s = str(input())
i = 0
tot = 0

while i < len(s):
    if 64 < ord(s[i]) < 91:
        tot += 1
    i += 1

print(tot)
