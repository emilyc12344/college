#!/usr/bin/env python3

tot = 0
i = 0
j = 0
k = 0
s = input()

while k < 4:
    while s[j] != '+':
        j += 1
    x = int(s[i:j])
    tot += x
    k += 1
    j += 1
    i = j

print(tot + int(s[j:]))
