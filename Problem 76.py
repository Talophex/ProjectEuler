# -*- coding: utf-8 -*-
"""
Created on Wed Apr 02 09:35:04 2014

@author: Lucas
"""
import math

def digitfactorial(n):
    answer = 0
    for s in str(n):
        answer += math.factorial(int(s))
    return answer

def P74(n):
    chainarray = ([])
    chainarray.append(n)
    running = True
    while running:
        n = digitfactorial(n)
        if n not in chainarray:
            chainarray.append(n)
        else:
            running = False
    return len(chainarray)

answer = 0
for x in xrange(1,1000000):
    if P74(x) == 60:
        answer +=1

print answer