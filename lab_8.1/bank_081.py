#!/usr/bin/env python3

class BankAccount(object):
    def set_attributes(self, name, number, balance):
        self.number = number
        self.name = name
        self.balance = balance
    def print_attributes(self):
        print('Name: {}\nAccount number: {}\nBalance: {:.2f}'.format(self.name, self.number, self.balance))
    def deposit(self, moneyz):
        self.balance = self.balance + moneyz
