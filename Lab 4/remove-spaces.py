#!/usr/bin/env python3

s = str(input())
i = 0
ans = ''
while i < len(s):
    if s[i] != ' ':
        ans += s[i]
    i += 1

print(ans)
