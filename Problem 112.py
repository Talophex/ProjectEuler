# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/lucas/.spyder2/.temp.py
"""
from __future__ import division

def decreasing(n):
    n = str(n)
    for j in xrange(0,len(n)-1):
        if n[j+1] > n[j]:
            return False
    return True

def increasing(n):
    n = str(n)
    for j in xrange(0,len(n)-1):
        if n[j+1] < n[j]:
            return False
    return True

i = 101
bouncies = 0

running = True
while running:
    if not decreasing(i) and not increasing(i):
        bouncies += 1
    density = 100*bouncies/i
    if density == 99:
        running = False
        print bouncies
        print i
        print density/100
    i += 1