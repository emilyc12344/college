#!/usr/bin/env python3

import sys

uploads = sys.stdin.readlines()
users = {}
user_task = {}
i = -1

while ((i ** 2) ** 0.5) < len(uploads) + 1:
    file_user = uploads[i].split('/')
    status = uploads[i].split('.')
    if status[0] not in user_task:
        if file_user[0] not in users:
            users[file_user[0]] = 0
        if status[-1] != 'incorrect\n':
            users[file_user[0]] += 1
        user_task[status[0]] = True
    i -= 1

for file_user in users:
    print(file_user, users[file_user])
