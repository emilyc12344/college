#!/usr/bin/env python3

class File(object):

    def __init__(self, file):
        self.file = file
        self.line = []
        self.perm = {}
        self.can_r = []
        self.can_w = []

    def add_line(self, add):
        self.line.append(add)

    def add_permission(self, name, perm):
        if name in self.perm:
            self.perm[name] += str(perm)
        else:
            self.perm[name] = str(perm)
        if perm == 'r':
            self.can_r.append(name)
        elif perm == 'w':
            self.can_w.append(name)

    def del_permission(self, name, perm):
        if name in self.perm:
            curr = list(self.perm[name])
            if perm in curr:
                curr.remove(perm)
                self.perm[name] = curr
                if perm == 'r':
                    self.can_r.remove(name)
                elif perm == 'w':
                    self.can_w.remove(name)

    def can_read(self, name):
        return name in self.can_r

    def can_write(self, name):
        return name in self.can_r

    def __str__(self):
        ans = [f'File: {self.file}']
        ans_perm = []
        n = 0
        #print(self.perm)
        if len(self.line) != 0:
            for i in self.line:
                ans.append(i)
        if len(self.perm) != 0:
            key = sorted(list(self.perm.keys()))
            for k in key:
                #print(list(self.perm[k]))
                if (len(list(self.perm[k])) > 1):
                    ans_perm.append(f'{k}: {", ".join(list(self.perm[k]))}')
                elif (len(list(self.perm[k])) != 0):
                    ans_perm.append(f'{k}: {list(self.perm[k])[0]}')
                else:
                    n += 1
            if n != len(key):
                ans.append('Permissions:')
            for i in ans_perm:
                ans.append(i)
        ans = '\n'.join(ans)
        return ans
