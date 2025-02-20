#!/usr/bin/env python3

s = str(input())
i = 0
j = 0
c_i = 0
a = True

curr = s[0]

while i < (len(s) - 1) and a:
    #print(curr, s[i + 1])
    if curr == s[i + 1]:
        let = s[c_i:(i + 1)]
        print(let + let)
        a = False
    else:
        c_i += 1
        curr = s[c_i]
    i += 1
