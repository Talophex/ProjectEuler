# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:22:21 2012

@author: Lucas
"""

for den in xrange(11,99):
    for num in xrange(10,den):
        for digit in xrange(1,10):
            if (str(digit) in str(den)) & (str(digit) in str(num)):
                if ('0' not in str(num)) & ('0' not in str(den)):
                    for n in str(num):
                        if int(n) != digit:
                            for d in str(den):
                                if int(d) != digit:
                                    if float(num)/float(den) == float(int(n))/float(int(d)):
                                        print num
                                        print den
                                        print