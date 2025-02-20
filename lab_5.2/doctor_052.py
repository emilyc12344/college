#!/usr/bin/env python3

import sys

time = 0

for curr in sys.stdin:
    curr = curr.split()
    if int(curr[0]) < time:
        time = time + int(curr[-1])
    else:
        time = int(curr[0]) + int(curr[-1])

print(time)
