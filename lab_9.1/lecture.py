#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return f'goals: {self.goals}\npoints: {self.points}'

    def total(self):
        return (self.goals * 3) + self.points

    def __eq__(self, other):
        return self.total() == other.total()

def __main__():
    s1 = Score(3, 4)
    s2 = Score(0, 13)
    print(s1)
    print(s2)
    print(s1 == s2)

if __name__ == '__main__':
    __main__()
