#/usr/bin/env python3

import sys

ins = sys.stdin.readlines()

line = ins[0].strip().split()
line = [int(line[0]), int(line[1]), int(line[2])]
min, curr, max = int(line[0]), int(line[1]), int(line[2])
#print(line)

ins = ins[1:]
for comm in ins:
    comm = comm.strip().lower()
    if comm == 'up' and curr + 1 <= max:
        curr = curr + 1
    elif comm == 'down' and curr - 1 >= min:
        curr = curr - 1

print(curr)
