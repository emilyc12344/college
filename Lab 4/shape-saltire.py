#!/usr/bin/env python3

n = int(input())
i = 0
x = 0

while i < (n // 2):
    x += 2
    print((' ' * i) + '*' + (' ' * (n - x)) + '*')
    i += 1

print((' ' * (n // 2)) + '*')

y = 1
while i > 0:
    print((' ' * (i - 1)) + '*' + (' ' * (y)) + '*')
    i -= 1
    y += 2
