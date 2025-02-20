#!/usr/bin/env python3

import sys

nums = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen'
}
tens = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
}

for l in sys.stdin:
    n = l.strip().split()
    ans = ''
    for i in n:
        if len(i) == 3:
            ans = ans + ' one hundred'
        elif len(i) > 1 and int(i[-1]) > 0 and int(i[0]) != 1:
            ans = ans + ' ' + tens[int(i[0])] + '-' + nums[int(i[1])]
        elif len(i) > 1 and int(i[0]) != 1:
            ans = ans + ' ' + tens[int(i[0])]
        else:
            ans = ans + ' ' + nums[int(i)]
    print(ans[1:])
