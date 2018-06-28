# -*- coding: utf-8 -*-
"""
Created on Sun Nov 04 11:51:12 2012

@author: Lucas
"""

def isprime(n):
    for x in xrange(2,int(abs(n) ** 0.5 + 1)):
        if not n % x:
            return False
    if n == 1:
        return False
    return True

def truncleft(o,p):
    return int(str(o)[p:])

def truncright(q,r):
    return int(str(q)[:-r])

def truncprime(s):
    for i in xrange(1,len(str(s))):
        if not isprime(truncleft(prime,i)):
            return False
        if not isprime(truncright(prime,i)):
            return False
    return True

testprimes = list()
answer = 0

for x in xrange(11,1000001,2):
    if isprime(x):
        testprimes.append(x)

for prime in testprimes:
    if truncprime(prime):
        print prime
        answer += prime

print answer