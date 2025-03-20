#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(s):
    q = Stack()
    for char in s:
        if q.is_empty() and char in ')}]':
            return False
        else:
            q.push(char)
            if char == ')' and '(' in q.l:
                q.l.remove(')')
                q.l.remove('(')
            if char == ']' and '[' in q.l:
                q.l.remove(']')
                q.l.remove('[')
            if char == '}' and '{' in q.l:
                q.l.remove('}')
                q.l.remove('{')
            #print(q.l)
    if q.is_empty():
        return True
    else:
        return False
