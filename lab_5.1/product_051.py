#!/usr/bin/env python3

import sys

num = sys.stdin.readlines()[0].strip()

def mult(n):
    l = len(n)
    nums = []
    curr = 1
    for i in n:
        i = int(i)
        if i > 0:
            nums.append(i)
    for i in nums:
        curr = curr * i
    return curr

ans = mult(num)
while len(str(ans)) > 1:
    ans = mult(str(ans))

print(ans)
