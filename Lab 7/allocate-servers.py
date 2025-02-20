#!/usr/bin/env python3

s = input()
a = [-1000]
count = 1

if s == 'end':
    count = 0

while s != 'end':
    s = int(s)
    a.append(s)
    if s - a[0] - 1000 < 0:
        count += 1
    else:
        a.pop(0)
    s = input()
#print(servers)
print(count)
