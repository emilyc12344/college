#!/usr/bin/env python3

def histogram(nums, char):
    ans = ''
    for i in nums:
        ans = ans + (char * i) + ' '
    print(ans[:-1])

histogram([6, 2, 15 , 3, 20 , 5], '=' )