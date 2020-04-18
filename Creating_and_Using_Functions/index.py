#!/usr/bin/env python
def echo_message(message,number=1):
    for i in range (0, number):
        print(f"{message}")
echo_message(input("enter message "), int(input("enter number ")))
