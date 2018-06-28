# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:35:52 2012

@author: Lucas
"""
import lucaslib

def arepermutations(n,m):
    list0 = ([])
    list1 = ([])
    for char0 in str(n):
        list0.append(char0)
    for char1 in str(m):
        list1.append(char1)
    if sorted(list0) == sorted(list1):
        return True
    return False

for x in xrange(1001, 3000, 2):
    if lucaslib.isprime(x):
        for y in xrange(100, 4000, 2):
            if lucaslib.isprime(x + y) and lucaslib.isprime(x + 2*y):
                if arepermutations(x, x+y):
                    if arepermutations(x, x+2*y):
                        print x
                        print x+y
                        print x+2*y
                        print