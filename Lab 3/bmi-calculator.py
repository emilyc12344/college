#!/usr/bin/env python3

w = int(input())
h = int(input())

bmi = w / (h * h) * 10000

if bmi < 18.5:
    print('underweight')
elif 18.5 <= bmi < 25:
    print('normal')
elif 25 <= bmi < 30:
    print('overweight')
else:
    print('obese')
