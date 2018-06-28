# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 13:27:50 2012

@author: Lucas
"""

str0 = ''
i = 1
while str0.__len__() < 1000000:
    str0 += str(i)
    i += 1
answer = 1
for x in xrange(0,7):
    answer *= int(str0[10**x-1])
print answer