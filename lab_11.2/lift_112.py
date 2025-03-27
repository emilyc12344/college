#!/usr/bin/env python3

import sys

def min_button_presses(f, s, g, u, d):
    if s == g:
        return 0

    queue = [(s, 0)]  
    visited = set([s])  

    while queue:
        current, steps = queue.pop(0)

        for next_floor in (current + u, current - d):
            if 1 <= next_floor <= f and next_floor not in visited:
                if next_floor == g:
                    return steps + 1  
                queue.append((next_floor, steps + 1))
                visited.add(next_floor)

    return "Sorry Sheila!"  

def main():
    i = sys.stdin.readline().strip().split()
    f = int(i[0])
    s = int(i[1])
    g = int(i[2])
    u = int(i[3])
    d = int(i[4])
    
    ans = min_button_presses(f, s, g, u, d)

    print(ans)

if __name__ == "__main__":
    main()

