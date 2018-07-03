# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 19:13:49 2016

@author: Lucas
"""

import fractions
import lucaslib
import sympy

def phi(n):
    result = 0
    for i in xrange(1,n+1):
        if fractions.gcd(n,i) == 1:
            result += 1
    return result
    
maxval = 2
for x in xrange(2,1000000):
    if float(x)/sympy.totient(x) > maxval:
        maxval = float(x)/sympy.totient(x)
        print x
        print float(x)/sympy.totient(x)
        print