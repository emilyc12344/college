#!/usr/bin/env python3

import os
ans = 'Bingo!'

with open('start.txt') as f:
    next = f.readline()
    next = next[:-1]

while os.path.isfile(next):
    with open(next) as f:
        next = f.readline()
        next = next[:-1]

print(next)
