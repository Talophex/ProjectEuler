# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:28:05 2012

@author: Lucas
"""

from __future__ import division

def diophants(n):
    raw = ([])
    cooked = ([])
    for x in xrange(n+1,n*2+1):
        y = (n*x)/(x-n)
        if y == int(y):
            current = ([])
            current.append(x)
            current.append(int(y))
            current.sort()
            raw.append(current)
            for item in raw:
                if item not in cooked:
                    cooked.append(item)
    return cooked

maxsols = 1
i = 120120
running = True
while running:
    if len(diophants(i)) > maxsols:
        maxsols = len(diophants(i))
        print i
        print len(diophants(i))
        print
    if len(diophants(i)) > 1000:
        running = False
    if i > 1000000:
        print 'Too high... Quitting.'
        running = False
    i += 60