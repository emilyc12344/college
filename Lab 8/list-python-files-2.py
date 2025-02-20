#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][0] != ".":
        with open(files[i]) as f:
            x = len(f.readlines())
            if files[i][-3:] == '.py' and x >= 1:
                print(files[i])
    i = i + 1
