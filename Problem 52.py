# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 08:06:14 2012

@author: Lucas
"""
def sortedlist(n):
    srtlst = ([])
    for char in str(n):
        srtlst.append(char)
    list.sort(srtlst)
    return srtlst

i = 1
running = True
while running:
    list1 = sortedlist(i)
    list2 = sortedlist(2 * i)
    list3 = sortedlist(3 * i)
    list4 = sortedlist(4 * i)
    list5 = sortedlist(5 * i)
    list6 = sortedlist(6 * i)

    if list1 == list2:
        if list2 == list3:
            if list3 == list4:
                if list4 == list5:
                    if list5 == list6:
                        print i
                        running = False
    if str(i)[0] == 2:
        i = 5 * i
    if i == 1000000:
        print i
        running = False
    i += 1
    