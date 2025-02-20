#!/usr/bin/env python3

import sys

n = {}

line = sys.stdin.readlines()

nums = sorted(line[0].strip().split())
let = line[1].strip()

n['A'] = nums[0]
n['B'] = nums[1]
n['C'] = nums[2]
n['D'] = nums[3]
n['E'] = nums[4]
n['F'] = nums[5]

ans = ''

for i in let:
    ans = ans + ' ' + str(n[i])
print(ans[1:])
