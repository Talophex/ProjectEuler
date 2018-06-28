# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 11:04:53 2012

@author: Lucas
"""

extdatafile = open('data.txt', 'r')
rawextdata = str(extdatafile.readline())
extdata = ([])
for a in rawextdata.split(','):
    extdata.append(int(a.strip(' ').strip('\n')))

alphabet = (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

possiblekeys = ([])

for letter1 in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            current = ([])
            current.append(ord(letter1))
            current.append(ord(letter2))
            current.append(ord(letter3))
            possiblekeys.append(current)

for key0_ in possiblekeys:
    for i in xrange(3,1205):
        key0_.append(key0_[i-3])

for m in xrange(0,len(possiblekeys)):
    xoredlist = ([])
    for n in xrange(0,1201):
        xoredlist.append(chr(possiblekeys[m][n] ^ extdata[n]))
    xoredstr = ''
    for char_ in xoredlist:
        xoredstr += str(char_)
    if '{' not in xoredstr and '}' not in xoredstr:
        if 'beginning' in xoredstr:
            print xoredstr
            break

answer = 0
for char999_ in xoredstr:
    answer += ord(char999_)
print answer