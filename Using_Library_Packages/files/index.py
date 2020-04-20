#!/usr/bin/env python

import os
path = "/home/grzesiek/Python3_learing_admin/Using_Library_Packages/files/ducks.txt"
ducks_file = open(path, "r", encoding="utf=8")
print(ducks_file.read())
print(ducks_file.read())