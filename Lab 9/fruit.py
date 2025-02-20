#!/usr/bin/env python3

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
list = sys.stdin.readlines()

while i < len(list):
    curr = list[i][:-1]
    if curr in fruit:
        print(curr)
    i += 1
