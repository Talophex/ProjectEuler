# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:16:13 2012

@author: Lucas
"""

import lucaslib

maxpan = 0
for x in xrange(1,10000):
    for y in xrange(3,12):
        current = ''
        for z in xrange(1,y):
            current += str(x*z)
        if lucaslib.pandigital(current):
            if current > maxpan:
                maxpan = current
                print x
                print y
                print maxpan
                print