#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.time = {}
    def add_time(self, dis, t):
        self.time[dis] = t
    def get_time(self, dis):
        return self.time[dis]
    def sum_time(self):
        return sum(self.time.values())
    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.sum_time()}'
