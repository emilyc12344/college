#!/usr/bin/env python3

s = input()
while s != 'end':
    a = s.split()
    s_t = int(a[1])
    e_t = s_t + int(a[2]) - 1
    e_t = str(e_t) + ':50'
    s_t = str(s_t) + ':00'
    a[1] = s_t
    a[2] = e_t
    print(*a)
    s = input()
