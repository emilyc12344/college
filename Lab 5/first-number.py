#!/usr/bin/env python3

s = str(input())
i = 0
j = 0
a = True

while i < len(s) and a:
    if (ord('0') - 1) < ord(s[i]) < (ord('9') + 1):
        j = i
        a = False
    i += 1

a = True
while j < len(s) and a:
    j += 1
    if not ((ord('0') - 1) < ord(s[j]) < (ord('9') + 1)):
        a = False

if i < len(s):
    print(s[(i - 1):j], (i - 1))
