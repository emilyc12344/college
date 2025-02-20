#!/usr/bin/env python3

import sys
from math import sqrt

def main():
    for line in sys.stdin:
        line = line.strip().split()
        a, b, c = int(line[0]), int(line[1]), int(line[2])
        try:
            top = sqrt((b * b) - (4 * a *c))
            a1 = ((-1 * b) - top) / (2 * a)
            a2 = ((-1 * b) + top) / (2 * a)
            print(f'{a1:.1f}, {a2:.1f}')
        except:
            print('None')


if __name__ == '__main__':
    main()
