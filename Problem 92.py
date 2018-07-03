# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:07:17 2012

@author: Lucas
"""

ones = 0
eightynines = 0
for x in xrange(1,10000000):
    test = x
    running = True
    while running:
        current = 0
        for i in str(test):
            current += int(i) ** 2
        test = current
        if test == 1:
            ones += 1
            running = False
        if test == 89:
            eightynines += 1
            running = False
print ones
print eightynines