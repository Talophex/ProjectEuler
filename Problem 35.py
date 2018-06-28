# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:51:07 2012

@author: Lucas
"""

def isprime(n):
    for x in xrange(2,int(abs(n) ** 0.5 + 1)):
        if not n % x:
            return False
    return True

def circularprime(n):
    prime = 0
    if isprime(n):
        for z in xrange(1,len(str(abs(n)))):
            if not isprime(int(rotate(str(n),z))):
                prime = prime + 1
        if prime == 0:
            return True
    else:
        return False

def inttolist(i):
    return [int(x) for x in str(i).zfill(9)]

def listtoint(l):
    return int("".join(str(x) for x in l))
    
def rotate(strg,n):
    n = n % len(strg)
    return strg[n:] + strg[:n]

answer = 4
for x in xrange(11,1000000, 2):
    if not "0" in str(x):
        if circularprime(x):
            answer = answer + 1
print answer
    