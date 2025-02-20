#!/usr/bin/env python3

import sys

f_name = sys.argv[1]
score = []
name = []

try:
    with open(f_name, 'r') as f:
        line = f.readline().strip()
        while line:
            #print(line)
            line = line.split()
            score.append(int(line[0]))
            name.append(' '.join(line[1:]))
            line = f.readline().strip()
    #print(score, name)
    i = score.index(max(score))
    print(f'Best student: {name[i]}\nBest mark: {max(score)}')
except FileNotFoundError:
    print(f'The file {f_name} could not be opened.')
