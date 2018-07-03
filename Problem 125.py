# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:38:18 2013

@author: Lucas
"""
import lucaslib
import math

squares_list = []
for a in xrange(1,100000):
    squares_list.append(a**2)
    
pal_list = []

sum_cap = 100000000

for i in xrange(1,int(math.sqrt(sum_cap))+1):
    current = 0
    for j in xrange(i, int(math.sqrt(sum_cap))+1):
        current += j**2
        if current > sum_cap:
            break
        if lucaslib.palindrome(str(current)):
            if current not in squares_list:
                pal_list.append(current)

pal_list = set(sorted(pal_list))
print pal_list
answer = 0
for pal in pal_list:
    answer += pal
print answer