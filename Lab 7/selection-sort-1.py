#!/usr/bin/env python3

a = input()
nums = []
si = 0

while a != 'end':
    nums.append(int(a))
    a = input()

small = nums[0]
i = 1
while i < (len(nums)):
    if nums[i] < small:
        small = nums[i]
        si = i
    i += 1

print(si)
