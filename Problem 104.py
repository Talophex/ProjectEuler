# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:59:46 2012

@author: Lucas
"""

import lucaslib

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]

fib1 = 1
fib2 = 1
i = 2
running = True
while running:
    fib1, fib2, i = fib2, int(str(fib1 + fib2)[-9:]), i+1
    if lucaslib.pandigital(str(fib2)[-9:]):
        if lucaslib.pandigital(str(fib(i))[:9]):
            print i
            running = False
    if i > 1000000:
        print "I'm so high..."
        running = False