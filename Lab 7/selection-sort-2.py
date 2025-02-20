#!/usr/bin/env python3

a = input()
nums = []

while a != 'end':
    nums.append(int(a))
    a = input()

i = int(input())
small = nums[i]
si = i
while i < (len(nums) - 1):
    if nums[i] <= small:
        small = nums[i]
        si = i
    i += 1

print(si)
