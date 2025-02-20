#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "dog", "cat", "mouse"]

i = 0
b = True

while i < len(a) and b:
    if len(a[i]) >= 6:
        print(a[i])
        b = False
    i += 1
