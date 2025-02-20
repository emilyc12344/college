#!/usr/bin/env python3

import sys

snap = {}
i = 0
list = sys.stdin.readlines()

while i < len(list):
    if list[i] not in snap:
        snap[list[i]] = True
    else:
        if list[i] != list[i - 1]:
            print('snap:', list[i][:-1])
            i = len(list) + 1
    i += 1
