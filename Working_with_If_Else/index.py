#!/usr/bin/env python

user = {'admin': True, 'active': True, 'name':'Grzegorz'}
prefix = ""

if user['admin'] and user ['active']:
    prefix = "(ACTIVE) + (ADMIN)"
elif user['admin']:
    prefix = "(ADMIN)"
elif user['active']:
    prefix = "(ACTIVE)"

print(prefix +"  "+ user['name'])