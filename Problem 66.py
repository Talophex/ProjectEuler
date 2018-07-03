# -*- coding: utf-8 -*-
"""
Created on Tue Jan 01 12:48:06 2013

@author: Lucas
"""
import math

squares = set([])
for x in xrange(1,10000000):
    squares.add(x**2)
    
maxsofar = 1
for D in xrange(2,1000):
    if D not in squares:
        for sq in squares:
            if D*sq+1 in squares:
                if int(math.sqrt(D*sq+1)) > maxsofar:
                    print D
                    print int(math.sqrt(D*sq+1))
                    print
                    maxsofar = int(math.sqrt(D*sq+1))
                break