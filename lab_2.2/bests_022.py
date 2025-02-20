#!/usr/bin/env python3

import sys

f_name = sys.argv[1]
score = []
name = []
best = []

def bob(f_name):
    i = 0
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
        b_mark = max(score)
        amount = score.count(b_mark)

        while i < amount:
            index = score.index(b_mark)
            best.append(name[index])
            score[index] = ''
            i += 1
            #print(best)
        #print(name)
        students = ', '.join(best)
        print(f'Best student(s): {students}\nBest mark: {b_mark}')

    except FileNotFoundError:
        print(f'The file {f_name} could not be opened.')
        return

bob(f_name)
