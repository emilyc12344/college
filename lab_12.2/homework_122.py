#!/usr/bin/env python3

import sys

def q_nums(s):
    qs = s.strip().split(';')
    count = 0
    for curr in qs:
        if '-' in curr:
            n1 = int(curr[:curr.index('-')])
            n2 = int(curr[curr.index('-')+1:])
            count += (n2 - n1) + 1
        else:
            count += 1
    return count

print(q_nums(sys.stdin.readline()))
