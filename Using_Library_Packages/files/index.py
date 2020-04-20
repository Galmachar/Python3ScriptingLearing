#!/usr/bin/env python
import os
path = "/home/grzesiek/Python3_learing_admin/Using_Library_Packages/files/ducks.txt"
ducks_file = open(path, "r", encoding="utf=8")

new_ducks = open('new_ducks.txt', 'a')

new_ducks.write(ducks_file.read())