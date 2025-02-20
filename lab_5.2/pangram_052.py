#!/usr/bin/env python3

import sys

a = 'qwertyuioplkjhgfdsazxcvbnm'
a = sorted(a)

for line in sys.stdin:
    missing = ''
    line = ''.join(sorted([i.lower() for i in line if i.isalnum()]))
    for i in a:
        if i not in line:
            missing = missing + i
    if len(missing) > 0:
        print('missing', missing)
    else:
        print('pangram')
