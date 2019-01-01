# -*- coding: utf-8 -*-
"""
Created on Mon May 04 14:19:22 2015

@author: Lucas
"""

testlength = 10000000

factorarray= []
for a in xrange(0,testlength):
    factorarray.append(0)


for i in xrange(1,testlength):
    for j in xrange(i,testlength,i):
        factorarray[j] += 1

answer = 0

for z in xrange(0,len(factorarray)-1):
    if factorarray[z] == factorarray[z+1]:
        answer += 1

print answer