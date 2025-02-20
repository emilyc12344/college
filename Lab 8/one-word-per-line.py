#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()

s = ''.join(s)
s = s.replace(' ', '\n')
s = s.replace('\n\n', '\n')
print(s[:-1])
