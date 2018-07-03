# -*- coding: utf-8 -*-
"""
Created on Fri May 01 13:12:18 2015

@author: Lucas
"""
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

mindiff = 1.0

for i in xrange(8,1000001):
    if i%7 != 0:
        testval = 3.0/7.0 - (math.floor(3.0/7.0*i))/float(i)
        if testval < mindiff:
            if gcd(int(math.floor(3.0/7.0*i)),int(i)) == 1:
                mindiff = testval
                print testval
                print i
                print