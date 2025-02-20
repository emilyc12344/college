#!/usr/bin/env python3

import sys

tot = 0
nums = sys.stdin.readline()

while len(nums) > 0:
    tot += int(nums)
    nums = sys.stdin.readline()

print(tot)
