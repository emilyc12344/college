#!/usr/bin/env python3

def calculator(arg):
    arg = arg.split()
    if len(arg) == 1:
        return float(arg[0])
    else:
        nums = []
        oper = []
        for i in arg:
            if i.replace('.', '').isnumeric():
                nums.append(float(i))
            else:
                oper.append(i)
        ans = nums.pop()
        for x in oper:
            if x == '/':
                ans = nums.pop() / ans
            elif x == '+':
                ans = ans + nums.pop()
            elif x == '*':
                ans = ans * nums.pop()
            elif x == '-':
                ans = nums.pop() - ans
            elif x == 'n':
                ans = ans * (-1)
            elif x == 'r':
                ans = ans ** 0.5
        if len(nums) == 0:
            return ans
        else:
            raise IndexError
