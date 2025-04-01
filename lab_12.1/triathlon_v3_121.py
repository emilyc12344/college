#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.time = {}
        self.all = []
    def add_time(self, dis, t):
        self.time[dis] = t
    def get_time(self, dis):
        return self.time[dis]
    def sum_time(self):
        return sum(self.time.values())
    def __eq__(self, other):
        return self.sum_time() == other.sum_time()
    def __lt__(self, other):
        return self.sum_time() < other.sum_time()
    def __gt__(self, other):
        return self.sum_time() > other.sum_time()
    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.sum_time()}'
class Triathlon(object):
    def __init__(self):
        self.data = {}
        self.all = {}
    def add(self, person):
        self.data[person.tid] = person.name
        self.all[person.sum_time()] = person
    def remove(self, tid):
        self.data.pop(tid)
    def lookup(self, tid):
        if tid in self.data:
            return Triathlete(self.data[tid], tid)
        else:
            return None
    def best(self):
        best = sorted(list(self.all))[0]
        return self.all[best]
    def worst(self):
        worst = sorted(list(self.all))[-1]
        return self.all[worst]
    def __str__(self):
        vals = list(self.data.values())
        sort = sorted(vals)
        keys = list(self.data.keys())
        ans = []
        for curr in sort:
            ans.append(f'Name: {curr}\nID: {keys[vals.index(curr)]}')
        return '\n'.join(ans)
