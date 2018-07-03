# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:01:57 2016

@author: Lucas
"""

minsofar = 1.0008

import lucaslib
import sympy

for i in xrange(5000001,10**7,2):
    if sorted(str(sympy.totient(i))) == sorted(str(i)):
        if i/float(sympy.totient(i)) < minsofar:
            print i
            if lucaslib.isprime(i):
                print "Prime!"
            print i/float(sympy.totient(i))
            print
            minsofar = i/float(sympy.totient(i))