#!/usr/bin/env python3

a = int(input())
b = int(input())

while b != 0:
    o_b = b
    b = a % b
    a = o_b

print(a)
