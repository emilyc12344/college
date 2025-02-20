#!/usr/bin/env python3

import sys

line = sys.stdin.read()

l_key = 'abcdefghijklmnopqrstuvwxyz'
u_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
i = 0


while i < len(line):
    if line[i] in l_key and line[i].islower():
        id = l_key.index(line[i])
        if (id + 13) >= len(l_key):
            jump = 13 - (len(l_key) - id)
        else:
            jump = id + 13
        ans = ans + l_key[jump]
    elif line[i] in u_key and line[i].isupper():
        id = u_key.index(line[i])
        if (id + 13) >= len(u_key):
            jump = 13 - (len(u_key) - id)
        else:
            jump = id + 13
        ans = ans + u_key[jump]
    else:
        ans = ans + line[i]
    i += 1

print(ans[:-1])
