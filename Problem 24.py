# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:25:44 2012

@author: Lucas
"""

import itertools

count = 1
list0 = ([0,1,2,3,4,5,6,7,8,9])
for x in itertools.permutations(list0):
    if count == 1000000:
        print x
        break
    count += 1