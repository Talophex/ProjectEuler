# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:41:37 2013

@author: Lucas
"""
import lucaslib

testprime = 3
nth = 1

nextprime = True
while nextprime:
    if lucaslib.isprime(testprime):
        nth += 1
        if ((testprime-1)**nth + (testprime+1)**nth)%(testprime**2) >= 10**10:
            print nth
            nextprime = False
    testprime += 2
    if nth >= 100000:
        nextprime = False