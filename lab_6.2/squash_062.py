#!/usr/bin/env python3

import sys
from re import findall

for line in sys.stdin:
    letters = findall(r'((.)\2*)', line)
    ans = ''
    for group, char in letters:
        ans = ans + (f'{len(group)}{char}')
    print(ans)
