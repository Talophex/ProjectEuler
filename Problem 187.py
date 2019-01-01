# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 20:48:19 2016

@author: Lucas
"""

testlim = 100000000

def primeslist(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

listofprimes = primeslist(int(testlim/2))
answer = []

for x in xrange(0,len(listofprimes)):
    for y in xrange(x,len(listofprimes)):
        if listofprimes[x]*listofprimes[y] > testlim:
            break
        else:
            answer.append(listofprimes[x]*listofprimes[y])

print len(answer)