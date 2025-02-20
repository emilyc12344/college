#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def drop():
    y = -2
    while (y * -1) < len(lines) + 1:
        for x in lines[y]:
            curr = lines[y].index(x)
            if x == 'S' and lines[y + 1][curr] == '.':
                lines[y + 1] = lines[y + 1][:curr] + 'S' + lines[y + 1][curr + 1:]
                lines[y] = lines[y][:curr] + '.' + lines[y][curr + 1:]
            #print(lines)
        y -= 1

i = 0
while i < (len(lines) * len(lines[0])):
    drop()
    i += 1

for i in lines:
    print(i.strip())
