# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:30:37 2012

@author: Lucas
"""
import math

maximum = 0
for p in xrange(10,1000):
    current = 0
    for x in xrange(1,p-1):
        for y in xrange(1,p-1):
            if x + y > p:
                break
            if x ** 2 + y ** 2 == (p-x-y) ** 2:
                current += 1
    if current/2 > maximum:
        maximum = current/2
        print p
        print maximum
        print