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
