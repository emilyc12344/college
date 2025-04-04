#!/usr/bin/env python3

class Vehicle(object):
    def __init__(self, reg, cat, mile, driver=None):
        self.reg = reg
        self.cat = cat
        self.mileage = mile
        if driver is None:
            driver = []
        self.drivers = driver
    def add_driver(self, drive):
        self.drivers.append(drive)
    def __str__(self):
        if len(self.drivers) > 1:
            driver = ', '.join(self.drivers)
        elif len(self.drivers) == 0:
            driver = ''
        else:
            driver = self.drivers[0]
        return 'Reg: {}\nCategory: {}\nMileage: {}\nDrivers: {}'.format(self.reg, self.cat, self.mileage, driver)
