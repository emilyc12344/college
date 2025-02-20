#!/usr/bin/env python3

s = input()
opts = []
i = 0

while s != 'end':
    a = s.split()
    opts.append(a)
    s = input()

day = input()
while i < len(opts):
    if opts[i][0] == day:
        print(*opts[i])
    i += 1
