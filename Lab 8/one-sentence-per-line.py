#!/usr/bin/env python3

s = input()
ans = ''
i = 0
j = 0
while s != 'end':
    i = 0
    a = s.split()
    while i < len(a):
        ans = ans + ' ' + a[i]
        i += 1
    s = input()

ans = ans[1:]
ans = ans.replace('.', '.\n')
ans = ans.replace('\n ', '\n')
ans = ans[:-1]
print(ans)
