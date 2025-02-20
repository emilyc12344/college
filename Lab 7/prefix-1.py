#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["dog", "cat", "mouse", "monttttttt", "montain"]
    s = "mont"

i = 0

while i < len(a):
    if s in a[i]:
        print(a[i])
    i += 1
