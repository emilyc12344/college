#!/usr/bin/env python3

def odd(nums):
    odds = []
    for n in nums:
        if n % 2 != 0:
            odds.append(n)
    return odds

def odd_2(nums):
    odds = [n for n in nums if n % 2 != 0]
    # what goes in final list | variable and iterable | condition
    return odds

def vowel(words): return ''.join([c for c in words if c not in 'aeiou'])

def even_square(nums): return [(n * n) for n in nums if n % 2 == 0]

def even_square_odd_cubed(nums): return [(n * n) if n % 2 == 0 else (n * n * n) for n in nums]

def palindrome(s): keep = ''.join([c for c in s if c.isalnum()]).lower(); return keep.lower() == keep[::-1]

test = 'baba'
print(palindrome(test))
