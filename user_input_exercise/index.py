#!/usr/bin/env python

#Write a script that prompts the user for:
#A file_name where it should write the content.
#The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.
#After the user enters an empty line, write all of the lines to the file and end the script.


import argparse
import sys

parser = argparse.ArgumentParser(description='lines ')
parser.add_argument('filename', help='file to open')
args = parser.parse_args()

def write_function():
    f = open(args.filename, "a+")
    x = input("Napisz co chcesz: ")
    if x != '':
        f.write(f"{x} \n")
      # f.write("\n")
        f.close()
        write_function()
    else:
        print("bye")
        f.close()

write_function()

