# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 13:50:59 2012

@author: Lucas
"""

def P120(a,n):
    return ((a-1)**n+(a+1)**n)%(a**2)

answer = 0

for a in xrange(3,1001):
    maxval = 0
    for n in xrange(1,a*2+1):
        if P120(a,n) > maxval:
            maxval = P120(a,n)
    answer += maxval

print answer