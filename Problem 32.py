# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:24:30 2012

@author: Lucas
"""

def pandigital(n):
    strn = str(n)
    if strn.count("0") > 0:
        return False
    for x in xrange(1,10):
        if strn.count(str(x)) == 0 or strn.count(str(x)) > 1:
            return False
    return True

panproducts = set([])
for i in xrange(1,1000):
    for j in xrange(100,10000):
        if pandigital(str(i) + str(j) + str(i*j)):
            print i
            print j
            print i*j
            print
            panproducts.add(i*j)

print panproducts
answer = 0
for prod in panproducts:
    answer += prod
print answer