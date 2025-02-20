#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
i = 2

with open(file_name, "w") as f:
    while i < len(sys.argv[0:]):
        message = sys.argv[i]
        f.write(message + '\n')
        i += 1
