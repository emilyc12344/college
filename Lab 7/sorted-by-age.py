#!/usr/bin/env python3

a = input()
nums = []
x = 0
y = 0
p = 0
i = 0
b = 0

while a != 'end':
    nums.append(a)
    a = input()

while x < len(nums):
    q = nums[x]
    str = q[6:8] + q[3:5] + q[0:2] + q[9:]
    nums[x] = str
    x += 1
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

while b < len(nums):
    print(nums[b][6:])
    b += 1
