# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:47:05 2015

@author: Lucas
"""
import lucaslib
import math

squares = []
for a in xrange(1,3334):
    squares.append(a**2)

def numdivisors(n):
    divs = 0
    for x in xrange(1,int(math.sqrt(n))+1):
        if n%x == 0:
            divs += 2
    return divs
    
ans = 0

for i in xrange(2,10000000):
    if i not in squares:
        if (i+1) not in squares:
            if numdivisors(i) == numdivisors(i+1):
                ans += 1

print ans