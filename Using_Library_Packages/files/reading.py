#!/usr/bin/env python

import os
path = "/home/grzesiek/Python3_learing_admin/Using_Library_Packages/files/ducks.txt"
ducks_file = open(path, "r", encoding="utf=8")
#print(ducks_file.read())
#.read() doesnt allow us to read second time!!
#print(ducks_file.read())

ducks_file.seek(0)
#print(ducks_file.read())

for line in ducks_file:
    print(line, end="") #end aby ladniej wygladalo
ducks_file.close() #zamkniecie pliku! - po zakonczeniu pracy z pliekiem trzeba zamknac plik
