#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return '{} {} {}'.format(self.name, self.phone, self.email)

class Contactlist(object):

    def __init__(self, d=None):
        if d is None:
            self.d = {}
        else:
            self.d = d

    def add(self, new):
        self.d[new.name] = new

    def remove(self, other):
        if other in self.d:
            self.d.pop(other)

    def get(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None

    def __str__(self):
        ans = ['Contact list\n', '------------']
        conts = []
        for i in list(self.d.values()):
            conts.append(str(i) + "\n")
        return f'{"".join(ans)}\n{"".join(sorted(conts))[:-1]}'
