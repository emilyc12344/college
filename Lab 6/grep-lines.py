#!/usr/bin/env python3

import sys

args = sys.argv[1]
s = input()

while s != 'end':
    if args in s:
        print(s)
    s = input()
