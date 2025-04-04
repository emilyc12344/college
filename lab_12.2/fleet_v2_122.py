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
        if len(list(self.v.keys())) > 0:
            d = self.update()
            if c in list(d.keys()):
                return d[c]
            else:
                return []
        else:
            return []

def main():
    v1 = Vehicle('221-D-34512', 'van', 9100, ['joe'])
    v2 = Vehicle('191-C-3213', 'car', 33000, ['mary'])
    v3 = Vehicle('241-OY-19767', 'car', 16000, ['max', 'joe', 'beatrice'])
    v4 = Vehicle('121-W-43111', 'van', 18212, ['martha', 'joe'])

    f = Fleet()

    van_drivers = f.get_drivers_by_category('van')
    assert(isinstance(van_drivers, list))
    assert(len(van_drivers) == 0)
    
    f.add(v1)
    f.add(v2)
    f.add(v3)
    f.add(v4)

    car_drivers = f.get_drivers_by_category('car')
    assert(isinstance(car_drivers, list))
    assert(len(car_drivers) == 4)
    for name in ['mary', 'max', 'joe', 'beatrice']:
        assert(name in car_drivers)
    
    lorry_drivers = f.get_drivers_by_category('lorry')
    assert(isinstance(lorry_drivers, list))
    assert(len(lorry_drivers) == 0)
if __name__ == '__main__':
    main()
