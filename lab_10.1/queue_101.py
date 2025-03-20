#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.l = []

    def enqueue(self, new):
        return self.l.append(new)

    def dequeue(self):
        return self.l.pop(0)

    def first(self):
        return self.l[0]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
