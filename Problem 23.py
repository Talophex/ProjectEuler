# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 11:50:22 2012

@author: Lucas
"""

def factor(n):
    factorlist = [1]
    for x in xrange(2, int((n ** .5) + 1)):
        if n % x == 0:
            factorlist.append(x)
            factorlist.append(n / x)  # find other factor in pair
    return factorlist

abundants = []
for x in xrange(1,28123):
    factors = factor(x)
    factors = list(set(factors)) #removes duplicates
    factorsum = sum(factors)
    if factorsum > x:
        abundants.append(x)

sumofabunds = []
for y in abundants:
    for z in abundants:
        sumofabunds.append(y + z)
    sumofabunds = list(set(sumofabunds))

testrange = []
for i in xrange(1,28123):
    testrange.append(i)

answer = [n for n in testrange if n not in sumofabunds]
print sum(answer)