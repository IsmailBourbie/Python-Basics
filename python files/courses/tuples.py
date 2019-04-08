# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:23:45 2019

@author: Ismail Bourbie
"""

te = (1, 2, "one") ## Create Tuple
t = te + (4, 5) ## Concatenate two tuples
tup = (1,) ## comma mean tuple with one element
t[0] ## get an element at an index
t[0:2] ## Get a Slice 

## use tuple to swap variables:
x = 2 
y = 3
(x, y) = (y, x)
print("x =", x, "and y =", y)


## use tuples to return more than one value
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)
(quot, rem) = quotient_and_remainder(8, 2)
print(quotient_and_remainder(8, 2))


## iterate over tuples
t_iter = (1, 4, 5, 9, 3, 19, 8)
def get_odd_num(t):
    odd_numbers = ()
    for i in t:
        if i%2 != 0:
            odd_numbers = odd_numbers + (i,)
    return odd_numbers

print(get_odd_num(t_iter))
    
    
    
    