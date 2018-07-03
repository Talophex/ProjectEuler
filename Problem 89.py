# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:28:14 2012

@author: Lucas
"""

def RomanToNumber(n):
    dictionary = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    romanarray = ([])
    for char in n:
        romanarray.append(dictionary[char])
    number = 0
    for i in xrange(0,len(romanarray)-1):
        if romanarray[i] >= romanarray[i+1]:
            number += romanarray[i]
        if romanarray[i] < romanarray[i+1]:
            number -= romanarray[i]
    number += romanarray[-1]
    return number

def NumberToRoman(n):
    dictionary = {1000:'M', 2000:'MM', 3000:'MMM', 4000:'MMMM', 100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM', 10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC', 0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
    intarray = ([])
    for int_ in str(n):
        intarray.append(int(int_))
    placedarray = ([])
    for i in xrange(0,len(intarray)):
        placedarray.append(intarray[i]*(10**(len(intarray)-i-1)))
    numeral = ''
    for j in placedarray:
        numeral += str(dictionary[j])
    return numeral

data = ([])
rawdata = open('data.txt', 'r')
for curline in rawdata:
    data.append(curline.strip('\n'))
answer = 0
for numeral_ in data:
    answer += len(numeral_) - len(NumberToRoman(RomanToNumber(numeral_)))
print answer