# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:58:22 2012

@author: Lucas
"""

answer = 0

for a in xrange(0,2):
    for b in xrange(0,3):
        for c in xrange(0,5):
            for d in xrange(0,11):
                for e in xrange(0,21):
                    for f in xrange(0,41):
                        for g in xrange(0,101):
                            if (200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g) > 200:
                                break
                            for h in xrange(0,201):
                                if (200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g +1*h) == 200:
                                    answer += 1
                                if (200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g +1*h) > 200:
                                    break
print answer