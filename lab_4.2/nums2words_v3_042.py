#!/usr/bin/env python3

import sys

nums = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten'
}

trans = {}

file = sys.argv[1]

with open(file) as f:
    lines = f.readlines()
    for l in lines:
        l = l.split()
        trans[l[0]] = l[1]

for l in sys.stdin:
    n = l.strip().split()
    ans = ''
    for i in n:
        ans = ans + ' ' + trans[nums[int(i)]]
    print(ans[1:])
