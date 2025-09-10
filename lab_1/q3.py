#!/usr/bin/env python3

class Memories(object):
    def __init__(self, **args):
        self.args = args
    def remember(self, check):
        if check in self.args.keys():
            print(self.args[check])
        else:
            print(False)

p1 = Memories(name='Tom', age=32, salary=50000)
p1.remember('salary')
p1.remember('email')