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

class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)

    def right_angle_triangle(self):
        sides = sorted([self.a.distance(self.b), self.b.distance(self.c), self.c.distance(self.a)])
        return (sides[-1]) ** 2 == (sides[0] ** 2) + (sides[1] ** 2)
