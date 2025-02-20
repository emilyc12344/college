#!/usr/bin/env python3

n = int(input())

n = (n // 100) % 100
n1 = n // 10
n2 = n % 10

print((n2 * 10) + n1)
