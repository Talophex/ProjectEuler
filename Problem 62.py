# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:27:03 2013

@author: Lucas
"""

cubes = ([])
pardigfreq = ([])

def digitfreq(n):
    freqarray = ([])
    for x in xrange(0,10):
        freqarray.append(str(n).count(str(x)))
    freqstr = ''.join(map(str, freqarray))
    return freqstr

#first integer to test, minimal speed improvement if guess is higher
i = 1

testinglength = 12

# find first integer with correct cube length
while len(str(i**3)) < testinglength:
    i += 1

while len(str(i**3)) == testinglength:
    cubes.append(i)
    pardigfreq.append(digitfreq(i**3))
    i += 1
    
for j in xrange(0,len(pardigfreq)):
    if pardigfreq.count(pardigfreq[j]) > 4:
        print cubes[j]
    