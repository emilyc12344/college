#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][0] != ".":
        with open(files[i]) as f:
            x = f.readlines()
            if (files[i][-3:] == '.py' and len(x) >= 1):
                print(files[i])
            elif len(x) >= 1 and x[0] == '#!/usr/bin/env python3\n':
                print(files[i])
    i = i + 1
