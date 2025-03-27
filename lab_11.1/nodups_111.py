#!/usr/bin/env python3

import sys

#lines = '\n'.join(sys.stdin.readlines()).split()
#print(lines)
ans = ''
seen = []

for line in sys.stdin:
    ans = ''
    if not(line[-2].isalnum()):
        char = line[-2]
        line = line[:-2]
        flag = 1
        #print(char)
    else:
        flag = 0
    #print(line[-2])
    for word in line.split():
        #print(word)
        if (word.lower() not in seen) and word[-1].isalpha():
            ans = ans + ' ' + word
            seen.append(word.lower())
        elif not (word.lower()[-1].isalnum()) and word.lower()[:-1] not in seen:
            ans = ans + ' ' + word
            seen.append(word.lower()[:-1])
        else:
            ans = ans + ' ' + '.'
    if flag == 1 and ans[-1] != '.':
        print(ans[1:] + char)
    else:
        print(ans[1:])
