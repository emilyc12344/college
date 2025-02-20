#!/usr/bin/env python3

import sys

nums = {
    'one': 'eins',
    'two': 'zwei',
    'three': 'drei',
    'four': 'vier',
    'five': 'funf',
    'six': 'sechs',
    'seven': 'sieben',
    'eight': 'acht',
    'nine': 'neun',
    'ten': 'zehn',
}

i = 0
list = sys.stdin.readlines()

while i < len(list):
    curr = list[i][:-1]
    if curr in nums:
        print(nums[curr])
    i += 1
