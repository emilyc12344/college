#!/usr/bin/env python3

a = True

# n + 1th hailstone number if n is eveb is n // 2
# n + 1th hailstone number if n is odd is n * 3 + 1
prev = int(input())
while a:
    curr = int(input())
    next = 0
    if prev % 2 == 0:
        next = prev // 2
    else:
        next = prev * 3 + 1
    if curr == next:
        print(prev, next)
        a = False
    else:
        prev = curr
