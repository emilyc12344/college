#!/usr/bin/env python3

import sys

temps = [int(i) for i in input().strip().split()]

i = 0
leastTemp = (0, max(temps) + 1)
while i < len(temps):
    if i < len(temps) - 2:
        tempMax = max([temps[i], temps[i+2]])
        if tempMax < leastTemp[1]:
            leastTemp = (i + 1, tempMax)
    i += 1
print(leastTemp[0], leastTemp[1])
