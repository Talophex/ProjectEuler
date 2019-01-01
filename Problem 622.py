# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:04:23 2018

@author: Lucas
"""
import time

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def P622(n):
    i = 1
    running = True
    while running:
        if (2**i)%(n-1) == 1:
            running = False
        elif i > 60:
            running = False
            return "Too high"
        else:
            i += 1
    return i

def abbrevback(k):
    eg = 2
    answer = 0
    running = True
    while running:
        if eg <= k/2:
            eg = 2*eg-1
        else:
            eg = (2*eg)%k
        answer += 1
        if eg == 2:
            running = False
    return answer

def shuffle(lst):
    shuffled = []
    for x in xrange(0,len(lst)/2):
        shuffled.append(lst[x])
        shuffled.append(lst[x+len(lst)/2])
    return shuffled

def shuffleback(n):
    deckstart = []
    for i in xrange(0,n):
        deckstart.append(i)
    deck = deckstart
    answer = 0
    running = True
    while running:
        newdeck = []
        for x in xrange(0,n/2):
            newdeck.append(deck[x])
            newdeck.append(deck[x+n/2])
        answer += 1
        if newdeck == deckstart:
            return answer
        elif answer > 1000:
            return "Too high"
        else:
            deck = newdeck
    
'''trialdeck = []
for a in xrange(0,6):
    trialdeck.append(a)

print trialdeck
for i in xrange(0,10):
    trialdeck = shuffle(trialdeck)
    print trialdeck
'''

'''
for x in xrange(4,10000,2):
    if P622(x) == 10:
        print x
'''

factorlst = []

for a in xrange(1,1073741824,2):
    if ((2**60)-1)%a == 0:
        factorlst.append(a+1)
        factorlst.append((((2**60)-1)/a)+1)

factorlst = set(factorlst)

finalanswer = 0
for fct in factorlst:
    if P622(fct) == 60:
        finalanswer += fct

print finalanswer