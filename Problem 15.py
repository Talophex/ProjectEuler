# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 11:14:38 2012

@author: Lucas
"""

series = ([])
series.append([1])
series.append([1,1])

for x in xrange(1,10):
    newseries = ([])
    newseries.append(1)
    for i in xrange(0,len(series[-1])-1):
        newseries.append(series[-1][i] + series[-1][i+1])
        newseries.append(1)
        series.append(newseries)
print series