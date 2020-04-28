#!/usr/bin/env python
import argparse

# build the parser

parser = argparse.ArgumentParser(description='Reads a file in reverse')
parser.add_argument('filename', help='file to read')
parser.add_argument('--limit', '-l', type=int, help='number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args)

# parse arguments

# reat the file, reverse the contents and print