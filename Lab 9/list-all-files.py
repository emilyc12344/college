#!/usr/bin/env python3

import os

a = ['.']
b = [0]

while len(b) > 0:
    files = os.listdir('.') + ['']
    if files[b[-1]] != files[-1]:
        if os.path.isdir(files[b[-1]]):
            os.chdir(files[b[-1]])
            a.append(files[b[-1]])
            b[-1] += 1
            b.append(0)
        else:
            print('/'.join(a) + '/' + files[b[-1]])
            b[-1] += 1
    else:
        a = a[:-1]
        b = b[:-1]
        os.chdir('..')
