# -*- coding: utf-8 -*-
"""
Created on Sat Nov 03 22:35:33 2012

@author: Lucas
"""

def isprime(n):
    for x in xrange(2,int(abs(n) ** 0.5 + 1)):
        if not n % x:
            return False
    return True

max = 45000
answer = set([])
primes = list()
squares = list()
cubes = list()
quartes = list()
for i in xrange(2,max):
    if isprime(i):
        primes.append(i)
for p in primes:
    squares.append(p ** 2)
    cubes.append(p ** 3)
    quartes.append(p ** 4)
for s in squares:
    for c in cubes:
        for q in quartes:
            if s + c + q < 50000000:
                answer.add(s + c + q)
            if s + c + q > 50000000:
                break
print len(answer)