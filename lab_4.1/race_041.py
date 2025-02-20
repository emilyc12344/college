#!/usr/bin/env python3

import sys

run = {}

def time(t):
    s = t.index(':')
    sec = (t[s + 1:])
    min = (t[:s])
    return [int(min), int(sec)], t

for line in sys.stdin:
    line = line.strip().split()
    name = line[0]
    line.remove(line[0])
    #print(line)
    try:
        for i in line:
            time(i)
        run[name] = (sorted(line)[0])
        #print(run)
    except:
        pass

key = list(run.keys())
val = list(run.values())
#print(val)
i = 0
while i < len(key):
    val[i] = [time(val[i]), key[i]]
    i += 1

best = sorted(val)[0]
print(f"{best[-1]}: {best[0][1]}")

