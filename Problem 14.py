# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 11:21:15 2012

@author: Lucas
"""

def iseven(n):
    if (n % 2) == 0:
        return True
    return False

maxchain = 0
for x in xrange(1,1000000):
    chain = 1
    candidate = x
    while candidate > 1:
        if iseven(candidate):
            candidate = candidate / 2
        else:
            candidate = 3 * candidate + 1
        chain = chain + 1
    if chain > maxchain:
        maxchain = chain
        print "Starting number:", x, "produces chain of:", maxchain
        