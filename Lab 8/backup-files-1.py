#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][0] != ".":
        if files[i][-4:] != '.bak':
            with open(files[i] + '.bak', 'w') as f1:
                with open(files[i]) as f2:
                    data = f2.read()
                    f1.write(data)
    i = i + 1
