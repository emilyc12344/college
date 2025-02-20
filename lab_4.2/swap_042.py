#!/usr/bin/env python3

def swap_keys_values(d):
    new = {}
    i = 0
    k = list(d.keys())
    v = list(d.values())
    while i < len(k):
        new[v[i]] = k[i]
        i += 1
    return new
