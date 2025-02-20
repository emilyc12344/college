#!/usr/bin/env python3

h1 = str(input())
h2 = str(input())

if len(h1) == len(h2):
    print(h1 if h1 > h2 else h2)
elif len(h1) > len(h2):
    print(h1)
else:
    print(h2)
