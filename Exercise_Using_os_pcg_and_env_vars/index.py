#!/usr/bin/env python
#Environment variables are often used for configuring command line tools and scripts. Write a script that does the following:

#Prints the first ten digits of PI to the screen.
#Accepts an optional environment variable called DIGITS. If present, the script will print that many digits of PI instead of 10.

import math
import os

number = int(os.getenv("DIGITS") or 10)
print("%.*f" % (number, math.pi))