#!/usr/bin/env python3

n = str(input())
i = 0

while i < len(n):
    if n[i] == '.':
        print(n[:i])
        print(n[(i + 1):])
    i += 1
