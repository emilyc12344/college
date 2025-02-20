#!/usr/bin/env python3

import sys
from re import findall

def main():
    for line in sys.stdin:
        p = '[A-Z]+'
        print(max(findall(p, line), key=len))

main()
