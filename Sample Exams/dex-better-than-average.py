#!/usr/bin/env python3

import sys

names = []
scores = []
marks = 0
total = 0
i = 0

curr = sys.stdin.readline()

while len(curr) > 0:
    line = curr.split()
    marks += int(line[-1])
    total += 1
    names.append(' '.join(line[:2]))
    scores.append(int(line[-1]))
    curr = sys.stdin.readline()

avg = marks // total

while i < len(scores):
    if scores[i] > avg:
        print(names[i])
    i += 1
