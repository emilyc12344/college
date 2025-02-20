#!/usr/bin/env python3

import sys
ans = ''

with open('irish-dobs.txt') as f:
    s = f.readlines()
    i = 0
    while i < len(s):
        x = s[i].split('/')
        day = x[0]
        x[0] = x[1]
        x[1] = day
        ans = ans + '/'.join(x)
        i += 1
f.close()

with open('american-dobs.txt', 'w') as f:
    f.write(ans)
