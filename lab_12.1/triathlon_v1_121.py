#!/usr/bin/env python3

class Triathlete(object):
  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
  def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}'

class Triathlon(object):
    def __init__(self):
        self.data = {}
    def add(self, person):
        self.data[person.tid] = person.name
    def remove(self, tid):
        self.data.pop(tid)
    def lookup(self, tid):
        if tid in self.data:
            return Triathlete(self.data[tid], tid)
        else:
            return None
