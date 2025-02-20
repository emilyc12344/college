#!/usr/bin/env python3

d = str(input())
i = 0
c = 0
prev_i = 0
ans = ''

while i < len(d):
    if d[i] == ' ' and c == 0:
        day = d[:i]
        prev_i = i
        i += 1
        c += 1
    elif d[i] == ' ' and c == 1:
        date = d[(prev_i + 1):i]
        prev_i = i
        i += 1
        c += 1
    elif d[i] == ' ' and c == 2:
        month = d[(prev_i + 1):(i - 1)]
        prev_i = i
        i += 1
        c += 1
    else:
        year = d[(prev_i + 1):]
    i += 1

print(month, date + ',', year, '(' + day + ')')
