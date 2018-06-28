# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:11:16 2012

@author: Lucas
"""
xbyx = 1
diagsum = 1
i = 1
running = True
while running:
    for x in xrange(0,4):
        i += xbyx + 1
        diagsum += i
    xbyx += 2
    if xbyx == 1001:
        running = False
print diagsum