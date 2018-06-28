# -*- coding: utf-8 -*-
"""
Created on Thu Sep 05 15:55:25 2013

@author: Lucas
"""
import math

def numcombinations(n,r):
    return (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))

count = 0

for i in xrange(1,101):
    print i
    for j in xrange(1,i+1):
        if numcombinations(i,j) > 1000000:
            count += 1
    print "Count: " + str(count)