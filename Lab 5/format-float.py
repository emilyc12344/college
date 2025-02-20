#!/usr/bin/env python3

n = str(input())
i = 0
p_i = 0

while i < len(n):
    if n[i] == '.':
        p_i = i
    i += 1
if not ('.' in n[p_i:]):
    print(n + '.0')
elif n[-1] == '.':
    print(n + '0')
elif n[0] == '.':
    print('0' + n)
elif n[:2] == '-.':
    print('-0' + n[1:])
else:
    print(n)
