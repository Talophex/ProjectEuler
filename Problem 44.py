# -*- coding: utf-8 -*-
"""
Created on Sat Nov 03 21:55:38 2012

@author: Lucas
"""

pentagonals = set([])
for i in xrange(1,10000):
    pentagonals.add(i * (3 * i - 1) / 2)
for x in pentagonals:
    for y in pentagonals:
        if (x + y) in pentagonals and (x - y) in pentagonals:
            print x
            print y
            print abs(x - y)