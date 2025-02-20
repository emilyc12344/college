#!/usr/bin/env python3

s = input()
i = 0
y = 0

while y < len(s):
    if s[y] == ',':
        print(s[:y])
        s = s[y + 1:]
        y = 0
    y += 1
print(s)

while False:
    print('hahahaha got you!')
