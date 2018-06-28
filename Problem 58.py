# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:44:51 2013

@author: Lucas
"""
import lucaslib

test = 1
primecount = 0
totalcount = 1.0
step = 2

running = True
while running:
    for x in xrange(0,4):
        test += step
        print test
        totalcount += 1.0
        if lucaslib.isprime(test):
            primecount += 1
    step += 2
    if primecount/totalcount < 0.10:
        print
        print "Prime count: " + str(primecount)
        print "Total count: " + str(totalcount)
        print "Side length: " + str(step-1)
        print
        running = False