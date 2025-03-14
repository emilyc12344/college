#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, h, m, d):
        self.hour = h
        self.minute = m
        self.duration = d

    def __str__(self):
        return '{:02}:{:02} ({} minutes)'.format(self.hour, self.minute, self.duration)
