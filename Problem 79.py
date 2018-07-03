# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:00:34 2012

@author: Lucas
"""
import itertools

def listception(small, big):
    for i in xrange(1 + len(big) - len(small)):
        if small == big[i:i+len(small)]:
            return True
    return False

data = ([])
rawdata = open('data.txt', 'r')
for curline in rawdata:
    cur = curline.strip('\n')    
    data.append(int(cur))

index = 70000090
running = True
while running:
    testarray = ([])
    for a in str(index):
        testarray.append(int(a))

    threearray = ([])
    for i in itertools.combinations(testarray, 3):
        test = ''
        for ch in i:
            test += str(ch)
        threearray.append(int(test))
    if set(data).issubset(set(threearray)):
        print index
        running = False
    index += 100