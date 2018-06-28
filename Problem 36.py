# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:45:55 2012

@author: Lucas
"""

import lucaslib

answer = 0
for x in xrange(1,1000000):
    if lucaslib.palindrome(x):
        if lucaslib.palindrome(int(lucaslib.binary(x))):
            answer += x
            print x
print 'Answer is: ' + str(answer)