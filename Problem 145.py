# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:02:45 2013

@author: Lucas
"""
count = 0
for x in xrange(1,1000000000):
    if str(x)[::-1][:1] != '0':
        plusrev = x + int(str(x)[::-1])
        if '0' not in str(plusrev) and '2' not in str(plusrev) and '4' not in str(plusrev) and '6' not in str(plusrev) and '8' not in str(plusrev):
            count += 1
            print x + int(str(x)[::-1])
            print
print
print count
            