#!/usr/bin/env python3

import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
a = True
i = 0
x = 0

with open(f1) as f:
    f1_lines = f.readlines()
    f.close()

with open(f2) as f:
    f2_lines = f.readlines()
    f.close()

while (i < len(f1_lines) and i < len(f2_lines)):
    if f1_lines[i] != f2_lines[i]:
        while f1_lines[i][x] == f2_lines[i][x]:
            #print(f1_lines[i][x], f2_lines[i][x])
            x += 1
        print(i, x)
        a = False
    i += 1

if a and len(f1_lines) != len(f2_lines):
    print(i, x)
#print(f1_lines, f2_lines)
