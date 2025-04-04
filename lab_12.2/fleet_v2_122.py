#!/usr/bin/env python3

class Vehicle(object):
    def __init__(self, reg, cat, mile, driver):
        self.reg = reg
        self.cat = cat
        self.mileage = mile
        self.drivers = driver
    def __str__(self):
        if len(self.drivers) > 1:
            self.drivers = ', '.join(self.drivers)
        else:
            self.drivers = self.drivers[0]
        return 'Reg: {}\nCategory: {}\nMileage: {}\nDrivers: {}'.format(self.reg, self.cat, self.mileage, self.drivers)

class Fleet(object):
    def __init__(self):
        self.v = {}
    def add(self, veh):
        self.v[veh.reg] = veh
    def remove(self, veh):
        if veh in self.v:
            self.v.pop(veh)
    def lookup(self, r):
        if r in self.v:
            return self.v[r]
        return None
    def update(self):
        d = {}
        cats = []
        for curr in self.v:
            if self.v[curr].cat not in cats:
                cats.append(self.v[curr].cat)
        for curr in cats:
            d[curr] = []
        for curr in self.v:
            if len(self.v[curr].drivers) > 1:
                for i in self.v[curr].drivers:
                    if i not in d[self.v[curr].cat]:
                        d[self.v[curr].cat].append(i)
            else:
                if self.v[curr].drivers[0] not in d[self.v[curr].cat]:
                    d[self.v[curr].cat].append(self.v[curr].drivers[0])
        return d
    def get_drivers_by_category(self, c):
        d = self.update()
        return d[c]
