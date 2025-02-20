#!/usr/bin/env python3

line = input()
line = input()
i = 0
tot = 0
while line != 'end':
    i = 0
    while line[i] != ',':
        i += 1
    if 'City,' in line:
        print(line[:i])
    line = input()
