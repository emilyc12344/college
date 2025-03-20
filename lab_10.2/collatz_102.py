#!/usr/bin/env python3

def collatz(n):
    print(n)
    if n % 2 == 0:
        return collatz(n // 2)
    elif n == 1:
        return n
    else:
        return collatz((n * 3) + 1)

from collatz_102 import collatz

def main():
    collatz(5)

if __name__ == '__main__':
    main()
