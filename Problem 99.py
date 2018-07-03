# -*- coding: utf-8 -*-
"""
Created on Mon May 04 11:18:39 2015

@author: Lucas
"""

import math

maxlog = 0

with open('data.txt') as inputfile:
    for linenum, line in enumerate(inputfile):
        base_, power_ = int(line.split(',')[0]), int(line.split(',')[1])
        if power_*math.log(base_) > maxlog:
            maxlog = power_*math.log(base_)
            print base_
            print power_
            print power_*math.log(base_)
            print linenum
            print

print maxlog