#!/usr/bin/env python3

import sys

tot = 0
x = 0
files = sys.argv[1:]
length = len(files)

while length > x:
    file_name = files[x]
    with open(file_name) as f:
        nums = f.readline()
        while len(nums) > 0:
            tot += int(nums)
            nums = f.readline()
    x += 1

print(tot)
