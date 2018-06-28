# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 11:38:44 2012

@author: Lucas
"""

terms = []
for x in xrange(2,101):
    for y in xrange(2,101):
        terms.append(x ** y)
terms = list(set(terms)) #removes duplicates
print len(terms)