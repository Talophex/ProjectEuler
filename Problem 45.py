# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:25:44 2012

@author: Lucas
"""

triangular = []
pentagonal = []
hexagonal = []

for i in xrange(100,100000):
    triangular.append(i*(i+1)/2)
    pentagonal.append(i*(3*i-1)/2)
    hexagonal.append(i*(2*i-1))
for hexagon in hexagonal:
    if hexagon in pentagonal:
        print hexagon