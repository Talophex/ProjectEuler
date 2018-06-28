# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:16:27 2012

@author: Lucas
"""

def alphanum(n):
    alphadict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    return alphadict[n]

def alphanumsum(n):
    answer = 0
    for char_ in n:
        answer += alphanum(char_)
    return answer

triangles = set([])
for x in xrange(1,100):
    triangles.add(int((x/2.0)*(x+1)))

fileobj = open('data.txt', 'r')
linestr = fileobj.readline()
linearray = str(linestr)
linearray = linearray.replace('"','')
array = linearray.split(',')

answer = 0
for word in array:
    if alphanumsum(word) in triangles:
        answer += 1
print answer