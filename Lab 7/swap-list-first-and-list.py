#!/usr/bin/env python3

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]

tmp = a[0]
a[0] = a[-1]
a[-1] = tmp

#print(a)
