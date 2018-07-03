# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:11:03 2016

@author: Lucas
"""
import lucaslib

def prob133(n):
    for x in xrange(5,6):
        if repunit(10**x)%n == 0:
            return False
    return True

def repunit(n):
    num = ''
    for x in xrange(0,n):
        num += '1'
    return int(num)
    
def divprime(n,p):
    return ""

legalfactors = []
for fac in lucaslib.factor(10000000000000000):
    legalfactors.append(fac)
    
primeslist = []
for pr in xrange(7,100000,2):
    if lucaslib.isprime(pr):
        primeslist.append(pr)

repunitdivs = []
for tst in primeslist:
    covered = []
    running = True
    i = 2
    caughtrem = repunit(i)%tst
    while running:
        if caughtrem == 0:
            if i in legalfactors:
                print tst
                repunitdivs.append(tst)
            running = False
        else:
            caughtrem = (10*caughtrem+1)%tst
            i += 1

print sum(primeslist)+5+3+2-sum(repunitdivs)