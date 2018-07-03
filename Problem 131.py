# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:38:29 2012

@author: Lucas
"""

def isprime(n):
    for x in xrange(2,int(abs(n) ** 0.5 + 1)):
        if not n % x:
            return False
    return True

answer = 0
cubes = set([])
j = 1
for i in xrange(2,578):
    cubes.add(i ** 3)
for x in xrange(1,1000000, 2):
    if isprime(x):
        running = True
        while running == True:
            for y in xrange(j, j + 13):
                z = x + (y ** 3)
                if z in cubes:
                    cubes.remove(z)
                    answer += 1
                    j = y
                    running = False
            running = False

print "Answer:"
print answer