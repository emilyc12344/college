#!/usr/bin/env python3

import sys

files = sys.argv[1:]
length = len(files)
x = 0
nums = 0

while x < length:
    with open(files[x]) as f:
        n = f.readline()
        while len(n) > 0:
            if ' ' in n:
                n = n.split()
                L = len(n) - 1
                while L >= 0:
                    nums += int(n[L])
                    L -= 1
            else:
                n = n[:-1]
                nums += int(n)
            n = f.readline()
    x += 1

print(nums)
