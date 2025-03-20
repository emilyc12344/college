#!/usr/bin/env python3

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    elif type(n) != list:
        n = [n, 1, 2]
    if len(n[1:]) != n[0]:
        n.append(n[-1] + n[-2])
        return fibonacci(n)
    else:
        return n[-1]
