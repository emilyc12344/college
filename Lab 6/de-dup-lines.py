#!/usr/bin/env python3

seen = []
a = 'T'
i = 0
s = input()
while s != 'end':
    i = 0
    a = 'T'
    while a == 'T' and i < len(seen):
        if s == seen[i]:
            a = 'F'
        i += 1
    if a == 'T':
        print(s)
    seen.append(s)
    s = input()
