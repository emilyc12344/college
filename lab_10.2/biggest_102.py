#!/usr/bin/env python3

def biggest(nums):
    if nums is None:
        return ''
    elif len(nums) == 1:
        return nums[0]
    elif nums[0] > nums[1]:
        nums.remove(nums[1])
    elif nums[1] > nums[0]:
        nums.remove(nums[0])
    return biggest(nums)
