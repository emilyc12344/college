#!/usr/bin/env python3

import os

files = os.listdir(".")
dir = []

i = 0
while i < len(files):
    if os.path.isfile(files[i]):
        print('./' + files[i])
    elif os.path.isdir(files[i]):
        dir.append(files[i])
    i += 1

dirs = (os.listdir(dir[0]))

while len(dirs) > 0:
    j = 0
    while j < len(dirs):
        if os.path.isfile(files[j]):
            print('./' + dirs[0] + '/' + files[j])
        elif os.path.isdir(dirs[0]):
            print(os.listdir(dirs[0]))
        j += 1
    dirs = (os.listdir(dir[0]))
