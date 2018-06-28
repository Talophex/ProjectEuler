# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:52:02 2012

@author: Lucas
"""

i = 7
fib1 = 3
fib2 = 5
fib3 = 8
running = True
while running:
    fib3 += fib2
    fib1 = fib2
    fib2 = fib3 - fib1
    fiblen = str.__len__(str(fib3))
    if fiblen == 1000:
        print i
        running = False
    i += 1
    if i > 100000:
        running = False