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

for l in sys.stdin:
    n = l.strip().split()
    ans = ''
    for i in n:
        ans = ans + ' ' + nums[int(i)]
    print(ans[1:])
