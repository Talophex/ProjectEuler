# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:04:21 2012

@author: Lucas
"""
answer = 0
for x in xrange(2,1000000):
    sum = 0
    for char in str(x):
        sum += int(char) ** 5
    if sum == x:
        answer += x
print answer
