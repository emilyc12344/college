#!/usr/bin/env python3

import sys

seen = {}

def check(el):
    return seen[el]

for i in sys.stdin:
    seen[i.strip()] = (i.count('aa') + i.count('ee')  + i.count('ii') + i.count('oo') + i.count('uu'))

print(sorted(seen, key=check, reverse=True)[0])
