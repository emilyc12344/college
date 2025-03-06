#!/usr/bin/env python3

import sys

class IPv4Network(object):

    def __init__(self, address=None, mask=None):
        self.address = address
        self.mask = mask

    def on_network(self, check):
        return self.address == check

def main():

    net = IPv4Network("136.206.140.250", "255.255.255.252")

    print(net.on_network("136.206.140.249"))
    print(net.on_network("136.206.140.252"))
    print(net)

if __name__ == '__main__':
    main()
