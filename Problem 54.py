# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:43:35 2015

@author: Lucas
"""

import math
import lucaslib

def ordercards(n):
    values = dict(zip('23456789TJQKA',range(2,15)))
    return sorted(n,key=lambda x:values[x[0]])

def flush(n):
    suits = set([])
    cardvals = []
    for card in n:
        cardvals.append(card[0])
        suits.add(card[1])
    for n,i in enumerate(cardvals):
        if i == 'T':
            cardvals[n] = '10'
        elif i == 'J':
            cardvals[n] = '11'
        elif i == 'Q':
            cardvals[n] = '12'
        elif i == 'K':
            cardvals[n] = '13'
        elif i == 'A':
            cardvals[n] = '14'
    if len(suits) == 1:
        score = 9000 + int(cardvals[4])
        return [True,score]
    return [False]
    
def straight(n):
    cardvals = []
    for card in n:
        cardvals.append(card[0])
    for n,i in enumerate(cardvals):
        if i == 'T':
            cardvals[n] = '10'
        elif i == 'J':
            cardvals[n] = '11'
        elif i == 'Q':
            cardvals[n] = '12'
        elif i == 'K':
            cardvals[n] = '13'
        elif i == 'A':
            cardvals[n] = '14'
    if cardvals == ['2','3','4','5','14']:
        return [True]
    elif int(cardvals[4])-int(cardvals[0]) == 4:
        if int(cardvals[1])-int(cardvals[0]) == 1:
            if int(cardvals[2])-int(cardvals[1]) == 1:
                if int(cardvals[3])-int(cardvals[2]) == 1:
                    if int(cardvals[4])-int(cardvals[3]) == 1:
                        return [True]
    return [False]
    
def FOURoak(n):
    suits = set([])
    cardvals = []
    for card in n:
        cardvals.append(card[0])
        suits.add(card[1])
    for n,i in enumerate(cardvals):
        if i == 'T':
            cardvals[n] = '10'
        elif i == 'J':
            cardvals[n] = '11'
        elif i == 'Q':
            cardvals[n] = '12'
        elif i == 'K':
            cardvals[n] = '13'
        elif i == 'A':
            cardvals[n] = '14'
    for val in set(cardvals):
        if cardvals.count(val) == 4:
            score = 8000 + int(cardvals[0])
            return [True, score]
    return [False]
    
def THREEoak(n):
    cardvals = []
    for card in n:
        cardvals.append(card[0])
    for val in set(cardvals):
        if cardvals.count(val) == 3:
            return True
    return False

def pair(n):
    cardvals = []
    for card in n:
        cardvals.append(card[0])
    for val in set(cardvals):
        if cardvals.count(val) == 2:
            return [True]
    return [False]

def two_pairs(n):
    cardvals = []
    valcount = []
    for card in n:
        cardvals.append(card[0])
    for val in set(cardvals):
        valcount.append(cardvals.count(val))
    if valcount.count(2) == 2:
        return [True]
    return [False]

def Full_House(n):
    if THREEoak(n):
        if pair(n):
            score = 7000
            cardvals = []
            for card in n:
                cardvals.append(card[0])
            for k,i in enumerate(cardvals):
                if i == 'T':
                    cardvals[k] = '10'
                elif i == 'J':
                    cardvals[k] = '11'
                elif i == 'Q':
                    cardvals[k] = '12'
                elif i == 'K':
                    cardvals[k] = '13'
                elif i == 'A':
                    cardvals[k] = '14'


answer = 0

i = 0
poker = open("Problem 54.txt")
for line in poker:

    testhand = ['TH','TH','TC','QS','TC']    
    
    unsplithand = line.split()
    hand1 = unsplithand[:5]
    hand2 = unsplithand[5:]
    hand1 = ordercards(hand1)
    hand2 = ordercards(hand2)
    if Full_House(hand1)[0]:
        print hand1
    i += 1
    