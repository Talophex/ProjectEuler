# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:17:06 2012

@author: Lucas
"""

import lucaslib

for x in xrange(3,1000):
    if lucaslib.isprime(x):
        running = True
        numerator = '9'
        while running:
            if int(numerator)%x == 0:
                print x
                print len(numerator)
                print
                running = False
            else:
                numerator += '9'
            if 10000%x == 0:
                running = False