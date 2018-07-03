# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 08:50:46 2012

@author: Lucas
"""

import math

def sumdigits(n):
    digitsum = 0
    for char in str(n):
        digitsum += int(char)
    return digitsum

answer = list()

catcher = 0
i = 11
running = True
while running:
    cur = sumdigits(i)
    for k in xrange(0,60):
        if math.pow(cur,k) == i:
            #print i
            answer.append(i)
            catcher += 1
            break
        if math.pow(cur,k) > i:
            break
    if catcher == 10:
        running = False
    i += 1
print answer