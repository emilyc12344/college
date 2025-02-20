#!/usr/bin/env python3

import sys

e_name = []
i = 0

with open('boys.txt') as f:
    b_name = f.readlines()

with open('girls.txt') as f:
    g_name = f.readlines()

while i < len(b_name):
    if b_name[i] in g_name:
        e_name.append(b_name[i])
    i += 1

curr = sys.stdin.readline()

while len(curr) > 0:
    if curr in e_name:
        print(curr[:-1], 'either')
    elif curr in g_name:
        print(curr[:-1], 'girl')
    else:
        print(curr[:-1], 'boy')
    curr = sys.stdin.readline()
