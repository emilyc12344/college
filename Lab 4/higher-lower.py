#!/usr/bin/env python3

curr = int(input())
a = 5
i = 0

while i < a:
    next = int(input())
    if curr > next:
        print('lower')
    elif curr == next:
        print('equal')
    else:
        print('higher')
    curr = next
    i += 1
