# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:14:06 2013

@author: Lucas
"""

import itertools
import lucaslib

def ConcPrime(a,b):
    if lucaslib.isprime(int(str(a)+str(b))):
        if lucaslib.isprime(int(str(b)+str(a))):
            return True
    return False

primes = ([3])
for i in xrange(7,1050,2):
    if lucaslib.isprime(i):
        primes.append(i)
primes.sort()

twoprimes = []
for j in xrange(0,len(primes)):
    newentry = [primes[j]]
    for pr in primes:
        if ConcPrime(newentry[0],pr):
            newentry.append(pr)
    if len(newentry) > 15:
        twoprimes.append(newentry)

for tst in itertools.combinations(twoprimes,4):
    print tst