# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:24:32 2016

@author: Lucas
"""

import lucaslib
import math
import sympy

answer = 0

for i in xrange(2,1000001):
    answer += sympy.totient(i)
print answer