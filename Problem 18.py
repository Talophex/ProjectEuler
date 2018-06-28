# -*- coding: utf-8 -*-
"""
Created on Tue Nov 06 08:09:38 2012

@author: Lucas
"""
def binary(n, digits=15):
    rep = bin(n)[2:]
    return ('0' * (digits - len(rep))) + rep
    
data = ([])
txtfile = open("data.txt")
for line in txtfile:
    part = [int(x) for x in line.split(',')]
    data.append(part)
txtfile.close()

maxsum = 0
counter = 1
running = True
while running:
    height = 0
    current = 0
    binpath = binary(counter)
    for i in xrange(0,len(binpath)):
        height += int(binpath[i])
        current += data[i][height]
    if current > maxsum:
        maxsum = current
        print binpath
        print maxsum
    if counter == 16380:
        running = False
    counter += 1