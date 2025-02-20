#!/usr/bin/env python3

import sys

# Binary search (adapted from CSC1003)
def binsearch(query, sorted_list):
    '''Return True if query in sorted_list otherwise False.'''

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        # print(f'{low} {mid} {high}')

        if sorted_list[mid] < query:
            # Search RHS
            low = mid + 1
        elif sorted_list[mid] > query:
            # Search LHS
            high = mid - 1
        else:
            # Found it
            return True

    # Not found
    return False

words = sys.stdin.read().splitlines()
w = [i.lower() for i in words if len(i) >= 5]
w = sorted(w)
ans = []
for i in w:
    if binsearch(i[::-1], w):
        ans.append(i)
'''
ans = []
for i in w:
    if i[::-1] in w:
        ans.append(i)
'''
for i in ans:
    if i.capitalize() in words:
        ans[ans.index(i)] = i.capitalize()

print(ans)

