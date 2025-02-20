#!/usr/bin/env python3

import sys

nums = sys.stdin.read().splitlines()
num = []
y = 0
a = True

for n in nums:
    num.append(n.split())

while y < len(num) and a:
    x = 0
    while x < len(num[y]) and a:
        try:
            if int(num[y][x]) > int(num[y][x - 1]) and int(num[y][x]) > int(num[y][x + 1]) and int(num[y][x]) > int(num[y - 1][x]) and int(num[y][x]) > int(num[y + 1][x]):
                print(int(num[y][x]))
                a = False
        except IndexError:
            pass
        x += 1
    y += 1

try:
    len(num[y])
except IndexError:
    print(-1)
