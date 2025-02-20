#!/usr/bin/env python3

s = str(input()) + ' '
i = 0
j = 0
a = True

while i < len(s) and a:
    if (ord('A') - 1) < ord(s[i]) < (ord('Z') + 1):
        j = i
        a = False
    i += 1

a = True
while j < len(s) and a:
    j += 1
    if not ((ord('A') - 1) < ord(s[j]) < (ord('Z') + 1)):
        a = False

if i < len(s):
    print(s[(i - 1):j], (i - 1))
