#!/usr/bin/env python3

def get_divisors(n):
    dev = []
    for i in range(1, n + 1):
        if n % i == 0:
            dev.append(i)
    return sorted(dev)

def get_proper_divisors(n):
    return get_divisors(n)[:-1]

def is_perfect(n):
    tot = 0
    for i in get_proper_divisors(n):
        tot += i
    return tot == n

def main():
    print(get_divisors(6))
    print(get_proper_divisors(6))
    print(is_perfect(6))


if __name__ == '__main__':
    main()
