#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
line = []
for l in lines:
	line.append(l.strip())

print(f'Words containing 17 letters: {[l for l in line if len(l) == 17]}')
print(f'Words containing 18+ letters: {[l for l in line if len(l) > 17]}')
print(f"Words with 4 a's: {[l for l in line if l.lower().count('a') == 4]}")
print(f"Words with 2+ q's: {[l for l in line if l.lower().count('q') >= 2]}")
print(f"Words containing cie: {[l for l in line if 'cie' in l]}") 
print(f"Anagrams of angle: {[l for l in line if sorted(l.lower()) == sorted('angle') and l != 'angle']}")