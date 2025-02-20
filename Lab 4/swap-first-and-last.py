#!/usr/bin/env python3

n = str(input())
s = (len(n) - 1)

print(n[-1] + n[1:s] + n[0])
