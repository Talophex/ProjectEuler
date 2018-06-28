# -*- coding: utf-8 -*-
"""
Created on Tue Jan 01 12:01:07 2013

@author: Lucas
"""
import lucaslib
import itertools

def Problem43(n):
    primes = ([2,3,5,7,11,13,17])
    for i in xrange(1,8):
        current = ''
        current += str(n)[i]
        current += str(n)[i+1]
        current += str(n)[i+2]
        if int(current)%primes[i-1] != 0:
            return False
    return True

answer = 0
for iter_ in itertools.permutations('0123456789', 10):
    num_ = ''
    for char_ in iter_:
        num_ += char_
    num_ = int(num_)
    if len(str(num_)) != 9:
        if Problem43(num_):
            answer += num_
print answer