# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:46:16 2019

@author: Ismail Bourbie
"""

def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    
    print("hi")
    return i%2 == 0

if(is_even(3)):
    print("Is even")
else:
    print("Is odd")
    

## Use keyword Args START:
print('----------keyword Args START:----------')
def printName(fname, lname, reverse = False): ## default value of reverse is True
    """
    
    Input: fname, a string
    Input: lname, a string
    Input: reverse, a Boolean
    Prints the concatenation of fname and lname depending in reverse value
    
    """
    
    if reverse:
        print(lname + ', ' + fname)
    else:
        print(fname, lname)

printName("BOURBIE", "Ismail", False) # BOURBIE Ismail
printName("BOURBIE", "Ismail", reverse = False) # BOURBIE Ismail
printName(lname = "Ismail", fname = "BOURBIE", reverse = False) # BOURBIE Ismail
printName("BOURBIE", "Ismail") # BOURBIE Ismail

print('----------keyword Args END.----------')
## Use keyword Args END.