#!/usr/bin/env python3

p_tot = 0
n_tot = 0
num = int(input())

if num < 0:
    n_tot = num
else:
    p_tot = num

while num != 0:
    num = int(input())
    if num > 0:
        p_tot += num
    else:
        n_tot += num


print(n_tot, p_tot)
