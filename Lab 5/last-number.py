#!/usr/bin/env python3

s = ' ' + str(input())
i = -1
x = 0
a = True

while a and (i * -1) < len(s):
    if (ord('0') - 1) < ord(s[i]) and ord(s[i]) < (ord('9') + 1):
        x = i
        while (s[x] != ' ') and (x * - 1) < len(s):
            x -= 1
        a = False
        if not ('0' <= s[-1] <= '9'):
            print(s[(x + 1):(i + 1)])
        else:
            s = s + ' '
            print(s[x:i])
    i -= 1
