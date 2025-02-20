#!/usr/bin/env python3

import sys

f_name = sys.argv[1]
score = []
name = []

def bob(f_name):
    try:
        with open(f_name, 'r') as f:
            line = f.readline().strip()
            while line:
                #print(line)
                line = line.split()
                try:
                    score.append(int(line[0]))
                    name.append(' '.join(line[1:]))
                except:
                    print(f'Invalid mark {line[0]} encountered. Exiting.')
                    return
                line = f.readline().strip()

        #print(score, name)
        i = score.index(max(score))
        print(f'Best student: {name[i]}\nBest mark: {max(score)}')

    except FileNotFoundError:
        print(f'The file {f_name} could not be opened.')
        return

bob(f_name)
