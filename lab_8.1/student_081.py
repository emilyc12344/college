#!/usr/bin/env python3

class Student(object):
    def set_attributes(self, sid, name, modlist):
        self.sid = sid
        self.name = name
        self.modlist = modlist
    def print_attributes(self):
        print('ID: {}\nName: {}\nModules: {}'.format(self.sid, self.name, ', '.join(self.modlist)))
    def add_module(self, newmod):
        if newmod not in self.modlist:
            self.modlist.append(newmod)
    def del_module(self, remmod):
        if remmod in self.modlist:
            self.modlist.pop(self.modlist.index(remmod))
