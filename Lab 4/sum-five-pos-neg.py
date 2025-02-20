#!/usr/bin/env python3

n = 5
n_tot = 0
p_tot = 0
i = 0

while i < n:
    num = int(input())
    if num > 0:
        p_tot += num
    else:
        n_tot += num
    i += 1

print(n_tot, p_tot)
