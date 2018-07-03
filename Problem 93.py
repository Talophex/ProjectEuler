# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:27:04 2013

@author: Lucas
"""
import lucaslib
import itertools
maxconsec = 0

for comb in itertools.combinations([1,2,3,4,5,6,7,8,9], 4):
    vallist = []
    for i in itertools.permutations(comb):
        for ops in itertools.product(['a','b','c','d'], repeat = 3):
            val = 0
            if ops[0] == 'a':
                val += i[0] + i[1]
            elif ops[0] == 'b':
                val += i[0] - i[1]
            elif ops[0] == 'c':
                val += i[0] * i[1]
            elif ops[0] == 'd':
                if str(i[1]) in lucaslib.factor(i[0]):
                    val += i[0] / i[1]
            if ops[1] == 'a':
                val += i[2]
            elif ops[1] == 'b':
                val -= i[2]
            elif ops[1] == 'c':
                val *= i[2]
            elif ops[1] == 'd':
                if str(i[2]) in lucaslib.factor(abs(val)):
                    val /= i[2]
            if ops[2] == 'a':
                val += i[3]
            elif ops[2] == 'b':
                val -= i[3]
            elif ops[2] == 'c':
                val *= i[3]
            elif ops[2] == 'd':
                if str(i[3]) in lucaslib.factor(abs(val)):
                    val /= i[3]
            if val not in vallist and val >= 1:
                vallist.append(val)
    vallist.sort()
    running = True
    i = 0
    while running:
        if vallist[i] != i+1:
            if i > maxconsec:
                print comb
                print i
                print
                maxconsec = i
            running = False
        i += 1
        