# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 08:40:00 2012

@author: Lucas
"""

def waystosum(n):
    val = ([])
    for fact1 in xrange(1,n-1):
        for multiple1 in xrange(1,n):
            for fact2 in xrange(1,n-1):
                for multiple2 in xrange(1,n):
                    if multiple1 * fact1 + multiple2 * fact2 == n:
                        val.append([fact1,multiple1,fact2,multiple2])
    return val

print waystosum(5)
print len(waystosum(5))/2