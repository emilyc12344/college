#!/usr/bin/env python3

import sys

args = sys.argv
tot = 0
i = 1
while i < len(args):
    tot += int(args[i])
    i += 1

print(tot)
