#!/usr/bin/env python3

import sys
lines = sys.stdin.read().split("\n")

open_lib = {"{": 0, "[": 0, "(": 0}
close_lib = {"}": 0, "]": 0, ")": 0}
translation_lib = {"}": "{", "]": "[", ")": "("}
positions = []

i = 0
while i < len(lines):
  brackets = {"t{": 0, "t[": 0, "t(": 0}
  cur = lines[i]
  pos = 0
  problem_pos = 0
  while pos < len(cur):
    temp = "t" + cur[pos]
    if cur[pos] in open_lib:
      positions.append(pos)
      brackets[temp] += 1
    if cur[pos] in close_lib:
      positions.append(pos)
      temp = "t" + translation_lib[cur[pos]]
      if brackets[temp] <= 0 and problem_pos == 0:
        problem_pos = pos
      else:
        brackets[temp] -= 1
    pos += 1
  if problem_pos == 0:
    if brackets["t{"] > 0 or brackets["t["] > 0:
      print(i, len(cur))
    if brackets["t("] > 0:
      print(i, len(cur))
  else:
    print(i, problem_pos)
  i += 1
