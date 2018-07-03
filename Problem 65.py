# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:56:18 2012

@author: Lucas
"""
import math
import fractions

numers = ([])
for x in xrange(1,34):
    numers.append(1)
    numers.append(2*x)
    numers.append(1)
numers.reverse()

numerator = 1
denominator = numers[0]
for i in xrange(0,len(numers)-1):
    numerator,denominator = denominator,denominator*numers[i+1]+numerator

numerator = 2*denominator+numerator

print numerator
print fractions.Fraction(numerator,denominator)

answer = 0
for ch in str(numerator):
    answer += int(ch)
print answer