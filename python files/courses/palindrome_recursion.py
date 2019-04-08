# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:00:14 2019

@author: Ismail Bourbie
"""

def isPalindrome (s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and isPalindrome(s[1 : -1])
isPalindrome("abcdcbas")