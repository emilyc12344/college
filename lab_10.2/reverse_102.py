#!/usr/bin/env python3

def reverse(s):
    if s == []:
        return s
    return [s[-1]] + reverse(s[:-1])
