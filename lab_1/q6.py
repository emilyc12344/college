#!/usr/bin/env python3

def filter_star(d, i):
    stars = '*' * i
    s = list(d.values())
    n = list(d.keys())
    x = 0
    while x < len(n):
        if s[x] == stars:
            print(n[x])
        x += 1

filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '****',
  'Generic Chocolates': '***'
}, 4) 