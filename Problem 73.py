# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:31:53 2016

@author: Lucas
"""
import bisect
import lucaslib
import math
import sympy

primes = [2]
for z in xrange(3,6500,2):
    if lucaslib.isprime(z):
        primes.append(z)

answer = 0
for i in xrange(2,12001):
    sieve = []
    for j in xrange(1,i):
        sieve.append(j)
    for p in xrange(0,bisect.bisect(primes,i)):
        if i%primes[p] == 0:
            for q in xrange(1,len(sieve)/primes[p]+1):
                sieve[primes[p]*q-1] = 0
    sieve = filter(lambda a: a != 0, sieve)
    answer += (bisect.bisect_left(sieve,i/2.0) - bisect.bisect_right(sieve,i/3.0))
print answer