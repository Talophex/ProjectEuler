# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 13:33:56 2012

@author: Lucas
"""

import lucaslib

def diophants0(n):
    rawlist = lucaslib.factor(n**2)
    rawlist.sort()
    cookedlist = ([])
    for item in rawlist:
        if item < n:
            cookedlist.append(item)
        else:
            break
    return len(cookedlist) + 1

maxsols = 0

for x in xrange(4,5,1):
    if diophants0(x) > maxsols:
        maxsols = diophants0(x)
        print x
        print diophants0(x)
        print