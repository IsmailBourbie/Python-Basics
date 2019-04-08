# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:30:34 2019

@author: Ismail Bourbie
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    
    ## comapre the smallest elemnt of the left list with the smallest element of the right list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
        
    ## if the right list is empty, append the left to result
    while (i < len(left)):
        result.append(left[i])
        i += 1
        
    ## if the left list is empty, append the right to result
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])         
        return merge(left, right)
    
testList = [1, 4, 6, 3, 0, 2, 8, 7, 9, 5]

print(merge_sort(testList))