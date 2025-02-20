#!/usr/bin/env python3

import sys

i = 19

print(' ' + ('-' * 20))
lines = sys.stdin.readlines()
nums = []
j = 0
while j < len(lines):
    coords = lines[j].strip().split()
    x = int(coords[0])
    y = int(coords[1])
    nums.append([x, y])
    j += 1

while i >= 0:
    s = list('|' + (' ' * 20) + '|')
    j = 0
    while j < len(nums):
        coord = nums[j]  # coord = [x, y]
        x = coord[0]
        y = coord[1]
        if i == y:
            s[x + 1] = '*'
        j += 1
    print("".join(s))
    i -= 1

print(' ' + ('-' * 20))
