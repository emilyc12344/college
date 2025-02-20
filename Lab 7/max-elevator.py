#!/usr/bin/env python3

a = input()
nums = []
ans = 0
x = 0
p = 0
i = 0
b = 0
tot = 0

while a != 'end':
    nums.append(int(a))
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

while (ans + nums[b]) < 500:
    ans += nums[b]
    b += 1
    tot += 1

print(tot, ans)
