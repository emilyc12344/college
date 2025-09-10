#!/usr/bin/env python3

def move_vow(s):
    vs = ''
    cs = ''
    vowels = 'aeiouAEIOU'
    for i in s:
        if i in vowels:
            vs = vs + i
        else:
            cs = cs + i
    return (vs + cs)

print(move_vow('This is DCU!'))