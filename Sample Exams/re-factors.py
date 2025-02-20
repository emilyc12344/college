#!/usr/bin/env python3

import sys

factor = sys.argv[1:]
i = 0
tot = 0

curr = sys.stdin.readline()[:-1]

while len(curr) > 0:
    while i < len(factor):
        if float((int(curr) // int(factor[i]))) == (int(curr) / int(factor[i])):
            tot += 1
        i += 1
    if tot == len(factor):
        print(curr)
    curr = sys.stdin.readline()
