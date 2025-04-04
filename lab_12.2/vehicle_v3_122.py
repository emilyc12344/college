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
        to_service = 10000 - (self.mileage % 10000)
        if self.mileage == 0:
            service = 'due in 10000 mile(s)'
        elif to_service == 10000:
            service = 'due now'
        else:
            service = f'due in {to_service} mile(s)'
        return 'Reg: {}\nCategory: {}\nMileage: {}\nDrivers: {}\nService {}'.format(self.reg, self.cat, self.mileage, driver, service)

def main():
    v1 = Vehicle('191-C-3213', 'car', 0, ['mary'])
    v2 = Vehicle('222-W-1', 'scooter', 1, ['beatrice'])
    print(v1)
    print(v2)
if __name__ == '__main__':
    main()
