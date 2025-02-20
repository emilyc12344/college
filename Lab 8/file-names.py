#!/usr/bin/env python3

import sys
names = []
files = sys.stdin.readline()
while len(files) > 0:
    files = files[:-1]
    files = files.split('/')
    files = files[-1]
    print(files)
    files = sys.stdin.readline()
