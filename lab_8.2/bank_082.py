#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, add):
        self.balance += add
    def withdraw(self, take):
        if self.balance - take >= 0:
            self.balance -= take
    def __str__(self):
        return f'Your current balance is {self.balance:.2f} euro'
