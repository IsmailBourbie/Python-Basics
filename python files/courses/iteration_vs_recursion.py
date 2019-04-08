# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:03:28 2019

@author: Ismail Bourbie
"""

## Multiplication using iterative sol START:
def multi_iterative(a, b):
    result = 0;
    while b > 0:
        result += a
        b -= 1
    return result
## Multiplication using iterative sol END.
    
## Multiplication using recursion sol START:
def multi_recursion (a, b):
    if b == 1:
        return a
    return a + multi_recursion(a, b-1)
## Multiplication using recursion sol END.

## factorial using iterative sol START:
def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
## factorial using iterative sol END.

## factorial using iterative sol START:
def fact_recursion(n):
    if n == 1: 
        return 1
    return n * fact_recursion(n-1)
    
## factorial using iterative sol END.
