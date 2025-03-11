#!/usr/bin/env python3

from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        midx = (self.x + other.x) / 2
        midy = (self.y + other.y) / 2
        return Point(midx, midy)

    def distance(self, other):
        return sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))

    def __str__(self):
        return f'({self.x:.1f}, {self.y:.1f})'

class Circle(object):

    def __init__(self, c=None, r=1):
        if c is None:
            c = Point(0, 0)
        self.radius = r
        self.centre = c

    def __str__(self):
        return 'Centre: {}\nRadius: {}'.format(self.centre, self.radius)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x) and (self.y != other.y)

    def __add__(self, other):
        nc = (self.centre.midpoint(other.centre))
        nr = self.radius + other.radius
        return Circle(nc, nr)

from circle_add_091 import Point, Circle

def main():
    p1 = Point()
    p2 = Point(4, 6)

    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)

    c3 = c1 + c2
    assert(isinstance(c3, Circle))
    print(c3)

if __name__ == '__main__':
    main()
