#!/usr/bin/env python3

import sys

i = 0
words = []
with open('translation.txt') as f:
    list = f.readlines()
    while i < len(list):
        words.append(list[i].split())
        i += 1

i = 0
list = sys.stdin.readlines()

while i < len(list):
    curr = list[i][:-1]
    j = 0
    while j < len(words):
        if words[j][0] == curr:
            print(words[j][1])
        j += 1
    i += 1
