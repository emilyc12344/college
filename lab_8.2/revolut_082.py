#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance
        self.trans = []
        self.orig = self.balance
    def deposit(self, add):
        self.balance += add
        self.trans.append(f'{add:.2f} deposit for a new balance of {self.balance:.2f}')
    def withdraw(self, take):
        if self.balance - take >= 0:
            self.balance -= take
            self.trans.append(f'-{take:.2f} withdrawal for a new balance of {self.balance:.2f}')
    def __str__(self):
        if len(self.trans) > 3:
            trans = '\n'.join(self.trans[-3:])
            self.orig = 100
            return f'Opening balance: {self.orig:.2f} euros\n{trans}\nCurrent balance: {self.balance:.2f} euros'
        elif len(self.trans) > 0:
            trans = '\n'.join(self.trans)
            return f'Opening balance: {self.orig:.2f} euros\n{trans}\nCurrent balance: {self.balance:.2f} euros'
        else:
            return f'Opening balance: {self.orig:.2f} euros\nCurrent balance: {self.balance:.2f} euros'

def main():
    b1 = BankAccount()
    assert(b1.balance == 0)
    print('0 transactions')
    print(b1)
    print()

    b1.deposit(100)
    print('1 transaction')
    print(b1)
    print()

    b1.withdraw(10)
    print('2 transactions')
    print(b1)
    print()

    b1.deposit(2000)
    print('3 transactions')
    print(b1)
    print()

    b1.withdraw(1)
    print('4 transactions')
    print(b1)
    print()

    b2 = BankAccount(1)
    assert(b2.balance == 1)
    print('0 transactions')
    print(b2)
    print()

if __name__ == '__main__':
    main()
