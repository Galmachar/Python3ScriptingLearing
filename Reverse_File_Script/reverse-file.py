#!/usr/bin/env python
import argparse
import sys
# build the parser

parser = argparse.ArgumentParser(description='Reads a file in reverse')
parser.add_argument('filename', help='file to read')
parser.add_argument('--limit', '-l', type=int, help='number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    # we can use just except: to handle any error 
    sys.exit(1) 
    #echo $? to print last exit status
else:
    with f:
        lines = f.readlines()
        lines.reverse()
        if args.limit: #if limit exists
            lines = lines[:args.limit]
        for line in lines:
            print(line.strip()[::-1]) #this is how to reverse string in python!
