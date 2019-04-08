# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:56:58 2019

@author: Ismail Bourbie
"""

## Sol Iterative
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = min(a, b)
    while a % i != 0 or b % i != 0:
        i -=1
    return i


## Sol Recursive
def gcdRecur(a, b):
    
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''    
    if b == 0:
        return a
    return gcdRecur(b, a % b)
