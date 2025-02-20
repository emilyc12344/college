#!/usr/bin/env python3

import sys

lines = []
word = {}

for l in sys.stdin:
    l = l.split()
    for line in l:
        line = line.lower()
        if not line.isalnum():
            line = ''.join(char for char in line if char.isalnum() or char == "'")
        if line in word:
            word[line] += 1
        else:
            word[line] = 1

key = list(word.keys())
val = list(word.values())

i = 0
while i < len(key):
    key[i] = [key[i], val[i]]
    i += 1

key = sorted(key)

i = 0
while i < len(key):
    print(f'{key[i][0]}: {key[i][1]}')
    i += 1
