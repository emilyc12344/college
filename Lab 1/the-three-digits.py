#!/usr/bin/env python3

num = int(input())

f_d = num % 10
s_d = (num % 100) - f_d
l_d = (num % 1000) - (s_d + f_d)

print(int(l_d / 100))
print(int(s_d / 10))
print(f_d)
