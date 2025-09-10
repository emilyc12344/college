#!/usr/bin/env python3

import sys
def sum(lists):
    tot = 0
    for l in lists:
        for i in l:
            if i % 2 == 0:
                tot += i
    return tot

print(sum([[1, 0, 2], [5, 5, 7], [9, 4, 3]]))