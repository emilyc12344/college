#!/usr/bin/env python3

curr = int(input())

while curr != 0 and next != 0:
    next = int(input())
    if next != 0:
        if curr > next:
            print('lower')
        elif curr == next:
            print('equal')
        else:
            print('higher')
    curr = next
