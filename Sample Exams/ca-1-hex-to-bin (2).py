#!/usr/bin/env python3

k1 = ',0000,0001,0010,0011,0100,0101,0110,0111,1000'
k2 = ',1001,1010,1011,1100,1101,1110,1111'
key = k1 + k2
n = input()
i = 0
c = 0
c_i = 0
x = 0
q = 0
d = 0
p = ''
ans = ''

while x < len(n) and n != 0:
    p = n[x]
    if '0' <= p <= '9':
        p = ord(p) - ord('0')
    else:
        p = ord(p) - ord('a') + 10

    i = 0
    c = 0
    a = True
    while i < len(key) and a:
        if key[i] == ',':
            c += 1
            c_i = i + 1
        if c == (p + 1):
            ans += key[c_i:(c_i + 4)]
            a = False

        i += 1
    x += 1

while n != 0 and q < len(ans) and ans[q] == '0':
    d += 1
    q += 1

if n == '0':
    print('0')
else:
    ans = ans[d:]
    print(ans)
