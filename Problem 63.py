# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:52:41 2012

@author: Lucas
"""

import lucaslib

answer = 0
for x in xrange(1, 100):
    for y in xrange(1, 100):
        if len(str(x ** y)) == y:
            print x
            print y
            print x ** y
            print
            answer += 1
print answer
