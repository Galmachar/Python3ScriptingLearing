#!/usr/bin/env python
# import time
from time import localtime, mktime, strftime
#kod z tutoriala: chujowy stoper z powodu braku milisekund: optymalna opcja do zrobienia, liczyc milisekundy zamaist sekund i pozniej konwertować na minuty godziny itd.  
def stoper():
    start_time = localtime()
    print(f"timer activated, starttime: {strftime('%X',start_time)}")
    input("Press 'Enter' to stop timer ")
    stop_time = localtime()
    difference = mktime(stop_time) - mktime(start_time)
    print(f"Timer stopped at {strftime('%X', stop_time)}")
    print(f"Total time: {difference} seconds")
stoper()
