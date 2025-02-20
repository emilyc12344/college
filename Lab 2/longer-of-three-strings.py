#!/usr/bin/env python3

a = str(input())
b = str(input())
c = str(input())

if len(a) > len(b) and len(a) > len(c):
    print(a)
elif len(b) > len(a) and len(b) > len(c):
    print(b)
else:
    print(c)
