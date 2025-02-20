#!/usr/bin/env python3

import sys

lines = []
vowels = ['a', 'e', 'i', 'o', 'u']
word = {}

for l in sys.stdin:
    l = l.lower().strip()
    for char in l:
        if (char in vowels):
            if char in word:
                word[char] += 1
            else:
                word[char] = 1

key = list(word.keys())
val = list(word.values())

i = 0
while i < len(key):
    val[i] = [val[i], key[i]]
    i += 1

val = sorted(val)[::-1]

for curr in val:
    print(f"{curr[1]}: {curr[0]: >{len(str(val[0][0]))}}")
