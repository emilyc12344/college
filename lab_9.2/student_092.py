#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, id, mod):
        self.name = name
        self.id = id
        self.mod = mod

    def avg(self):
        nums = []
        for i in self.mod:
            nums.append(int(i[1]))
        return round(sum(nums) / len(nums))

    def __str__(self):
        ans = ''
        ans += f'Name: {self.name}\nID: {self.id}\n'
        m = []
        for i in sorted(self.mod):
            m.append(i[0])
        ans += f'Modules: {", ".join(m)}\nAverage mark: {self.avg()}'
        return ans
