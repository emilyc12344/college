#!/usr/bin/env python3

import sys

words = sys.stdin.read().splitlines()
#print(words)

short = [i for i in words if ('a' in i) and ('e' in i) and ('i' in i) and ('o' in i) and ('u' in i)]
shortest = min(short, key=len)

iary = [i for i in words if i[-4:] == 'iary']

e = [i for i in words if 'e' in i]
max_e = 0
for i in e:
    if i.count('e') + i.count('E') > max_e:
        max_e = i.count('e') + i.count('E')

print(f'Shortest word containing all vowels: {shortest}')
print(f'Words ending in iary: {len(iary)}')
print(f"Words with most e's: {[i for i in e if max_e == i.count('e') + i.count('E')]}")
