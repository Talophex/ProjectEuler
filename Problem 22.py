# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:04:55 2012

@author: Lucas
"""

def namescore(word):
    score = 0
    for ltr in word:
        if ltr == "A":
            score += 1
        elif ltr == "B":
            score += 2
        elif ltr == "C":
            score += 3
        elif ltr == "D":
            score += 4
        elif ltr == "E":
            score += 5
        elif ltr == "F":
            score += 6
        elif ltr == "G":
            score += 7
        elif ltr == "H":
            score += 8
        elif ltr == "I":
            score += 9
        elif ltr == "J":
            score += 10
        elif ltr == "K":
            score += 11
        elif ltr == "L":
            score += 12
        elif ltr == "M":
            score += 13
        elif ltr == "N":
            score += 14
        elif ltr == "O":
            score += 15
        elif ltr == "P":
            score += 16
        elif ltr == "Q":
            score += 17
        elif ltr == "R":
            score += 18
        elif ltr == "S":
            score += 19
        elif ltr == "T":
            score += 20
        elif ltr == "U":
            score += 21
        elif ltr == "V":
            score += 22
        elif ltr == "W":
            score += 23
        elif ltr == "X":
            score += 24
        elif ltr == "Y":
            score += 25
        elif ltr == "Z":
            score += 26
    return score

data = ([])

import csv
with open('names.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data = row
data.sort()

answer = 0
for i in xrange(0,len(data)):
    answer += namescore(data[i]) * (i+1)

print answer