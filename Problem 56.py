# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:06:05 2012

@author: Lucas
"""
import math

def digitalsum(n):
    val = 0
    for i in str(n):
        val += int(i)
    return val

maximum = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        current = a ** b
        if digitalsum(current) > maximum:
            maximum = digitalsum(current)
            print a
            print b
            print maximum
            print