#!/usr/bin/env python3

mark = int(input())

print('first:', mark >= 70)
print('second:', 50 <= mark <= 69)
print('third:', 40 <= mark <= 49)
print('fail:', mark < 40)
