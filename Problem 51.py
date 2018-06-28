# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 09:50:42 2013

@author: Lucas
"""
def appendodd(n):
    oddlist = ([1,3,5,7,9])
    odded = ([])
    for i in oddlist:
        odded.append(int(str(n)+(str(i))))
    return odded

def insertx(n):
    inserted = ([])
    for x in xrange(0,len(str(n))):
        inserted.append(str(n)[:x]+'x'+str(n)[x:])
    return inserted

print insertx(123)