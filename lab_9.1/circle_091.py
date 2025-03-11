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

from circle_091 import Point, Circle

def main():
    p1 = Point(2, 3)
    c1 = Circle(p1, 5)
    assert(c1.centre is p1)
    assert(c1.radius == 5)

    c2 = Circle()
    assert(isinstance(c2.centre, Point))
    assert(c2.radius == 1)

    c3 = Circle()
    assert(c3.centre is not c2.centre)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()
