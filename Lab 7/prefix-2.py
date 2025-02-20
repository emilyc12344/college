#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["dog", "cat", "mouse", "monttttttt", "montain"]
    s = "mont"

i = 0
b = True

while i < len(a) and b:
    if s in a[i]:
        print(a[i])
        b = False
    i += 1
