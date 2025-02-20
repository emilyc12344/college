#!/usr/bin/env python3

s = input()
a = []

a = [0] * 999
i = 0

while s != "end":
  a[int(s)] = a[int(s)] + 1
  s = input()

while i < len(a):
  if a[i] != 0:
    if a[i] > 1:
      print(i)
      a[i] = a[i] - 1
      i = i - 1
    else:
      print(i)
  i = i + 1
