# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 08:19:12 2012

@author: Lucas
"""

def palindrome(n):
    if n == int(str(n)[::-1]):
        return True

answer = 0
for x in xrange(1,10000):
    ind = 1
    running = True
    cur = x + int(str(x)[::-1])
    while running:
        if palindrome(int(cur)):
            running = False
            #print "Palindrome:"
            #print cur
        cur += int(str(cur)[::-1])
        ind += 1
        if ind > 100:
            print "Lychrel:"
            print x
            answer += 1
            running = False
print answer