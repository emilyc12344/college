#!/usr/bin/env python3

import sys
url = sys.argv[1]

scheme = ''
host = ''
port = ''
path = ''
query = ''
fragment = ''

token = url.split('://')
scheme = token[0]
url = token[1]

token = url.split('?')
url = token[0]

if len(token) > 1:
    query = token[1]

token = url.split('/')
host_port = token[0]
path = '/' + '/'.join(token[1:])

token = host_port.split(':')
host = token[0]

if len(token) > 1:
    port = token[1]

token = url.split('#')
url = token[0]

if len(token) > 1:
    fragment = token[1]

print('scheme:', scheme)
print('host:', host)
if 0 < len(port):
    print('port:', port)
print('path:', path)
if 0 < len(query):
    print('query-string:', query)
if 0 < len(fragment):
    print('fragment-id:', fragment)
