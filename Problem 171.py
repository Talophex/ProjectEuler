# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:45:05 2013

@author: Lucas
"""
squares = set([])
for i in xrange(1,50):
    squares.add(i**2)

for x in xrange(1,1000000):
    sum = 0
    for n in str(x):
        sum += int(n)**2
    if sum in squares:
        print x
        print sum
        print