#!/usr/bin/env python3

#1 - 20, high, low, correct/ bert trusted, bert not trusted

import sys

log = sys.stdin.readlines()

guess = []
answer = []

i = 1
while i <= len(log):
    line = log[i - 1].strip()
    if i % 2 == 0:
        answer.append(line)
    else:
        guess.append(int(line))
    i += 1

i = 0
range = [1, 20]
while i < len(guess):
    if answer[i] == 'higher' and guess[i] > range[0]:
        range[0] = guess[i]
    elif answer[i] == 'lower' and guess[i] < range[1]:
        range[1] = guess[i]
    i += 1

if range[0] < guess[-1] < range[1]:
    print('Bert can be trusted')
else:
    print('Bert is not to be trusted')
