# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:08:21 2013

@author: Lucas
"""
import lucaslib

def nextprime(n):
    i = n + 2
    running = True
    while running:
        if lucaslib.isprime(i):
            return i
            running = False
        i += 2 #requires n to be odd, will fail if n = 2

SigmaS = 0

p1 = 5
p2 = 7

running0 = True
while running0:
    running1 = True
    i = 1
    while running1:
        if str(i*p2)[-len(str(p1)):] == str(p1):
            print p1
            print p2
            print str(i*p2)
            SigmaS += int(str(i) + str(p1))
            running1 = False
        i += 1
    p1 = p2
    p2 = nextprime(p1)
    if p1 > 100000:
        print SigmaS
        running0 = False