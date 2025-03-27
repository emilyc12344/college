#!/usr/bin/env python3

import sys

for word in sys.stdin:
    word = word.strip()
    ans = []
    i = 0
    while i < len(word):
        if word[i] in 'aeiou':
            ans.append(word[i])
            i += 3
        else:
            ans.append(word[i])
            i += 1
    print(''.join(ans))

