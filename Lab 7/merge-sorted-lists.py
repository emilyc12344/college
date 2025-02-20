#!/usr/bin/env python3

a = []
b = []
i = 0
j = 0
x = 0
ans = []
str = input()
while str != 'end':
    a.append(int(str))
    str = input()

str = input()
while str != 'end':
    b.append(int(str))
    str = input()

while len(a) > 0 and len(b) > 0:
    if a[0] < b[0]:
        print(a.pop(0))
    else:
        print(b.pop(0))

ans = a + b

while x < len(ans):
    print(ans[x])
    x += 1

#print(ans)
