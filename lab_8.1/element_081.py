#!/usr/bin/env python3

class Element(object):
    def set_attributes(self, number, name, symbol, bp):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.bp = bp
    def print_attributes(self):
        print('Number: {}\nName: {}\nSymbol: {}\nBoiling point: {} K'.format(self.number, self.name, self.symbol, self.bp))
