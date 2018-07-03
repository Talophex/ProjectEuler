# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:04:20 2012

@author: Lucas
"""

import lucaslib
import itertools
import time

def concat(a,b):
    str0 = str(a)+str(b)
    return str0

def abortpandigital(n):
    for i in xrange(1,10):
        if str(n).count(str(i)) > 1:
            return True
    return False

primes = ([])

digits = ([1,2,3,4,5,6,7,8,9])
for x in xrange(1,10):
    for y in itertools.permutations(digits,x):
        str0_ = ''
        for z in y:
            str0_ += str(z)
        int0_ = int(str0_)
        if lucaslib.isprime(int0_):
            primes.append(int0_)
primes.sort()

pairs = ([])
triplets = ([])
quartets = ([])
quintets = ([])
sextets = ([])
for i in xrange(0,len(primes)):
    for j in xrange(0,len(primes)):
        test0 = concat(primes[i],primes[j])
        if len(test0) > 9:
            break
        if abortpandigital(test0):
            break
        if lucaslib.pandigital(int(test0)):
            templist0 = [i,j]
            templist0.sort()
            if templist0 not in pairs:
                pairs.append(templist0)
        for k in xrange(0,len(primes)):
            test1 = concat(test0,primes[k])
            if len(test1) > 9:
                break
            if abortpandigital(test1):
                break
            if lucaslib.pandigital(int(test1)):
                templist1 = [i,j,k]
                templist1.sort()
                if templist1 not in triplets:
                    triplets.append(templist1)
            for m in xrange(0,len(primes)):
                test2 = concat(test1,primes[m])
                if len(test2) > 9:
                    break
                if abortpandigital(test2):
                    break
                if lucaslib.pandigital(int(test2)):
                    templist2 = [i,j,k,m]
                    templist2.sort()
                    if templist2 not in quartets:
                        quartets.append(templist2)
                for n in xrange(0,len(primes)):
                    test3 = concat(test2,primes[n])
                    if len(test3) > 9:
                        break
                    if lucaslib.pandigital(int(test3)):
                        templist3 = [i,j,k,m,n]
                        templist3.sort()
                        if templist3 not in quintets:
                            quintets.append(templist3)
                        break
                    for o in xrange(0,len(primes)):
                        test4 = concat(test3,primes[o])
                        if len(test4) > 9:
                            break
                        if lucaslib.pandigital(test4):
                            templist4 = [i,j,k,m,n,o]
                            templist4.sort()
                            if templist4 not in sextets:
                                sextets.append(templist4)
                            break

print len(pairs)
print len(triplets)
print len(quartets)
print len(quintets)
print len(sextets)
print len(pairs)+len(triplets)+len(quartets)+len(quintets)+len(sextets)