# -*- coding: utf-8 -*-
"""
author: Lucas Thomas
"""

import lucaslib
import itertools

listto9 = str(1234567)
maxpanprime = 0
for x in itertools.permutations(listto9):
    cooked = ''
    for char_ in x:
        cooked += char_
    if lucaslib.isprime(int(cooked)):
        if cooked > listto9:
            listto9 = cooked
            print cooked