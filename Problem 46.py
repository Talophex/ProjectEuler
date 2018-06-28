# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 10:47:07 2012

@author: Lucas
"""
import math

def isprime(n):
    for x in xrange(2,int(abs(n) ** 0.5 + 1)):
        if not n % x:
            return False
    if n == 1:
        return False
    return True

primelist = set()
primelist.add(2)
for x in xrange(3,10000,2):
    if isprime(x):
        primelist.add(x)
sumlist = set()
for y in primelist:
    for z in xrange(1,1000):
        sumlist.add(y + 2 * math.pow(z,2))


running = True
i = 9
while running:
    if not isprime(i):
        if i not in sumlist:
            print i
    i += 2
    if i > 10000:
        running = False