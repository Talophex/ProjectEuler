# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 17:06:46 2016

@author: Lucas
"""
import lucaslib

def repunit(n):
    num = ''
    for x in xrange(0,n):
        num += '1'
    return int(num)

primeslist = []
for pr in xrange(7,180000,2):
    if lucaslib.isprime(pr):
        primeslist.append(pr)

primefacs = []

for tst in primeslist:
    running = True
    i = 2
    caughtrem = repunit(i)%tst
    while running:
        if caughtrem == 0:
            if (10**9)%i == 0:
                primefacs.append(tst)
            running = False
        else:
            caughtrem = (10*caughtrem+1)%tst
            i += 1
            
print primefacs
answer = 0
for x in xrange(0,40):
    answer += 