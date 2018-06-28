# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:34:02 2012

@author: Lucas
"""

import math

factorialsum = 0
for x in xrange(3,1000000):
    currentfact = 0
    for n in str(x):
        currentfact = currentfact + math.factorial(int(n))
    if currentfact == x:
        factorialsum = factorialsum + currentfact
print factorialsum