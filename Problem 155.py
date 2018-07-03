# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:09:58 2012

@author: Lucas
"""

total = 1
additions = 1
for i in xrange(2,19):
    print i
    additions *= 2
    total += additions
    print total
    print