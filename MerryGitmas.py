# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:10:45 2020

@author: Lewis Shutler
@author: Thomas Cann
"""

#Shows how many days before christmas.
from datetime import datetime

def main():
    print("Merry Gitmas!")
    #Time now
    now = datetime.now()
    christmas = datetime(now.year, 12, 25)
    calculateDays(now)
    print_tree(7)
    
def print_segment(n, total_width):
    for size in range(1, n+1, 2):
        print((size * "*").center(total_width))

def print_tree(size):
    for i in range(3, size+1, 2):
        print_segment(i, size)

def calculateDays(now):
    difference = christmas.day - now.day
    if difference > 0:
        print(f"It is {difference} days till Christmas!")
    else:
        print("It is Christmas!")
        
if __name__ = '__main__' :
    main()


