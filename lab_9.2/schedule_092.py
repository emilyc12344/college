#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, h, m, d):
        self.hour = h
        self.minute = m
        self.duration = d

    def __str__(self):
        ans = '{:02}:{:02} ({} minutes)'.format(self.hour, self.minute, self.duration)
        return ans

class Schedule(object):

    def __init__(self):
        self.plan = []

    def add(self, new):
        self.plan.append(str(new))

    def __str__(self):
        ans = ['Schedule\n--------']
        for i in sorted(self.plan):
            ans.append(i)
        ans.append(f'Meetings today: {len(ans) - 1}')
        ans = '\n'.join(ans)
        return ans
