#!/usr/bin/env python3

a = input()
nums = []
x = 0
p = 0
i = 0

while a != 'end':
    nums.append(a)
    a = input()

while p < len(nums):
    small = nums[p]
    i = p + 1
    si = p
    while i < len(nums):
        if nums[i] < small:
            small = nums[i]
            si = i
        i += 1
    nums[si] = nums[p]
    nums[p] = small
    p += 1

while x < len(nums):
    print(nums[x])
    x += 1
