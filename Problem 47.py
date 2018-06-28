# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:59:36 2012

@author: Lucas
"""
import time

def isprime(n):
    for x in xrange(2,int(abs(n) ** 0.5 + 1)):
        if not n % x:
            return False
    return True

def factor(n):
    factorlist = []
    for x in xrange(2, int((n ** .5) + 1)):
        if n % x == 0:
            factorlist.append(x)
            factorlist.append(n / x)  # find other factor in pair
    return factorlist

running = True
i = 10000
while running:
    current0 = 0
    if isprime(i):
        current0 += 1
    for n in xrange(2, int((i/2) + 1)):
        if i % n == 0:
            if isprime(n):
                current0 += 1
    if current0 > 3:
        current1 = 0
        j = i + 1
        if isprime(j):
            current1 += 1
        for n in xrange(2, int((j/2) + 1)):
            if j % n == 0:
                if isprime(n):
                    current1 += 1
        if current1 > 3:
            current2 = 0
            k = i + 2
            if isprime(k):
                current2 += 1
            for n in xrange(2, int((k/2) + 1)):
                if k % n == 0:
                    if isprime(n):
                        current2 += 1
            if current2 > 3:
                print i
                current3 = 0
                m = i + 3
                if isprime(m):
                    current3 += 1
                for n in xrange(2, int((m/2) + 1)):
                    if m % n == 0:
                        if isprime(n):
                            current3 += 1
                if current3 > 3:
                    print str(current0) + str(current1) + str(current2) + str(current3)
                    print i
                    running = False
    i += 1