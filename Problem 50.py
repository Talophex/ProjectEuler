# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:24:19 2012

@author: Lucas
"""

import lucaslib

primes = ([])
for i in xrange(1,1000000):
    if lucaslib.isprime(i):
        primes.append(i)

maxconsec = 0
for i in xrange(0,len(primes)-600):
    for consec in xrange(500,600):
        current = 0
        for j in xrange(0,consec):
            current += primes[i+j]
        if current < 1000000:
            if primes.count(current) == 1:
                if consec > maxconsec:
                    maxconsec = consec
                    print i
                    print consec
                    print current
                    print
        else:
            break
print maxconsec
            