#!/usr/bin/env python3

import sys

for line in sys.stdin:
    letter = ''
    amount = 0
    i = 0
    ans = ''
    while i < len(line) - 1:
        if line[i] != line[i + 1] and line[i - 1] != line[i]:
            ans = ans + '1' + line[i]
        elif line[i] != letter:
            letter = line[i]
            amount = 2
        elif line[i] == line[i + 1]:
            amount += 1
        else:
            ans = ans + str(amount) + letter
            letter = ''
            amount = 0
        i += 1
    print(ans)
