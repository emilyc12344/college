#!/usr/bin/env python3

num = str(input())
a = True
ans = ''
while num != 'end':
    if a and num[0] == num[1]:
        ans = num
        a = False
    num = str(input())
if ans != '':
    print(ans)
