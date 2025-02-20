#!/usr/bin/env python3

mon = int(input())
day = int(input())

d_y = ((mon - 1) * 30) + day
print(((d_y + 6) % 7) + 1)
