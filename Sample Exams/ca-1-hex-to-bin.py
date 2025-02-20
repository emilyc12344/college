#!/usr/bin/env python3

key = ',0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111'
n = input()
i = 0
c = 0
c_i = 0
x = 0
q = 0
d = 0
p = ''
ans = ''
a = True

while i < len(key) and a:
    if p != n[x]:
        p = n[x]
        if not ('0' <= p <= '9'):
            if p == 'a':
                p = '10'
            elif p == 'b':
                p = '11'
            elif p == 'c':
                p = '12'
            elif p == 'd':
                p = '13'
            elif p == 'e':
                p = '14'
            elif p == 'f':
                p = '15'

    if key[i] == ',':
        c += 1
        c_i = i + 1

    if x < len(n) and c == (int(p) + 1):
        ans = ans + key[c_i:c_i + 4]
        x += 1
    i += 1

    if len(ans) == (len(n) * 4):
        a = False

a = True
while q < len(ans) and a:
    if ans[q] == '0':
        d += 1
    else:
        a = False
    ans = ans[d:]
    q += 1
print(ans)
