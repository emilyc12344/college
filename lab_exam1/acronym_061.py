#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    ans = ''
    for word in line:
        if word[0].isupper():
            ans = ans + word[0]
    print(ans)
