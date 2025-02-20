#!/usr/bin/env python3

line = input()
i = 0
tot = 0
while line != 'end':
    i = 0
    while line[i] != ',':
        i += 1
    if ',WI' in line:
        tot += 1
    line = input()
print(tot)
