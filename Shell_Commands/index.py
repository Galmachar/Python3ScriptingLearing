#!/usr/bin/env python
#https://docs.python.org/3/library/subprocess.html
import subprocess
proc = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#print(proc.stdout) #bytes object, not a string! raw information!
print(proc.stdout.decode()) 
