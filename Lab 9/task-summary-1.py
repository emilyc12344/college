#!/usr/bin/env python3

import sys

uploads = sys.stdin.readlines()
seen = {}
i = -1

while abs(i) < len(uploads) + 1:
    status = uploads[i].split('.')
    if status[-1] != 'incorrect\n' and status[0] not in seen:
        print(status[0] + '.' + status[1])
    seen[status[0]] = True
    i -= 1
