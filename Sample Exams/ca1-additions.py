#!/usr/bin/env python3

a = True

while a:
    i = 0
    s = 0
    tot = 0
    gap = 19
    n = str(input())
    if n != 'end':
        while i < len(n):
            if ord(n[i]) == 32:
                s = i
            i += 1
        n1 = n[:s]
        n2 = n[(s + 1):]
        tot = int(n1) + int(n2)
        num = (n1 + ' ' + '+' + ' ' + n2 + ' ' + '=')
        gap = gap - (len(num) - 1)
        if len(num) < 20:
            print((' ' * gap), num, tot)
        else:
            print(num, tot)
    else:
        a = False
