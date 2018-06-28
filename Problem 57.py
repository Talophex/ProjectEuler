# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:49:09 2013

@author: Lucas
"""

def addfractions(num0,den0,num1,den1):
    num_init = num0*den1+num1*den0
    den_init = den0*den1
    return ([num_init,den_init])