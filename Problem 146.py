# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 15:38:27 2014

@author: Lucas
"""
import lucaslib

def P146(n):
    testnum = n**2
    if lucaslib.isprime(testnum+1):
        if lucaslib.isprime(testnum+3):
            if lucaslib.isprime(testnum+5) == False:
                if lucaslib.isprime(testnum+7):
                    if lucaslib.isprime(testnum+9):
                        if lucaslib.isprime(testnum+13):
                            if lucaslib.isprime(testnum+27):
                                return True
    return False

for x in xrange(1,40):
    if lucaslib.isprime(x):
        print x