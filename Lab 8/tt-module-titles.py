#!/usr/bin/env python3

s = input()
i = 0
ans = ''
while s != 'end':
    a = s.split()
    i = 0
    b = a[5:]
    print(*b)
    '''
    while i < len(b):
        if i > 0:
            ans = ans + ' ' + b[i]
            i += 1
        else:
            ans = ans + b[i]
            i += 1
    '''
    s = input()
