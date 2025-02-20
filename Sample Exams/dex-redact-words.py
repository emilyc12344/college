#!/usr/bin/env python3

import sys

r_words = sys.argv[1:]
words = sys.stdin.readlines()
i = 0

while i < len(words):
    curr = words[i][:-1]
    if curr in r_words:
        rep = len(curr) * '*'
        words[i] = rep
    else:
        words[i] = words[i][:-1]
    i += 1

i = 0

while i < len(words):
    print(words[i])
    i += 1
