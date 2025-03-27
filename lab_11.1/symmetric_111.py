#!/usr/bin/env python3

import sys

n1 = []
n2 = []

n = sys.stdin.readlines()

while len(n) > 1:
    #print(n1, n2)
    n1.append(n.pop(0).strip())
    n2.append(n.pop(0).strip())

if len(n1) + len(n) + len(n2) == 1:
    ans = (''.join(n1) + ''.join(n) + ''.join(n2))[:-1]
elif len(n) > 0:
    ans = '\n'.join(n1) + '\n' + '\n'.join(n) + '\n'.join(n2[::-1])
else:
    ans = '\n'.join(n1) + '\n' + '\n'.join(n2[::-1])
print(ans)
