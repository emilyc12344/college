#!/usr/bin/env python3

import sys


last = [0, 0]
curr_max = 0

for line in sys.stdin:
    line = line.strip().split()
    dis = int(line[1]) - last[1]
    time = int(line[0]) - last[0]
    #print(line, dis, time)
    if time > 0:
        speed = dis // time
    else:
        speed = 0
    #print(speed)
    if speed > curr_max:
        curr_max = speed
    last = [int(line[0]), int(line[1])]

print(curr_max)
