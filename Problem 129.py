# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 21:12:56 2016

@author: Lucas
"""
import lucaslib
import math

def repunit(n):
    num = ''
    for x in xrange(0,n):
        num += '1'
    return int(num)
    
def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)
    
for x in xrange(1000001,1000100,2):
    if gcd(x,10) == 1:
        running = True
        i = len(str(x))+1
        caughtrem = repunit(i)%x
        while running:
            if caughtrem == 0:
                if i > 1:
                    print x
                    print i
#                print i
#                print
                running = False
            else:
                caughtrem = (10*caughtrem+1)%x
                i += 1