#!/usr/bin/env python

users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
]

for user in users:
    prefix = ""
    if user['admin']:
        prefix += "(ADMIN)"
    if user['active']:
        prefix += "(ACTIVE)"
    print(user['name'] + " " + prefix)