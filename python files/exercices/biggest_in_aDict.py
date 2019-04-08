# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:13:25 2019

@author: Ismail Bourbie
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = {"length": 0, "name": ""}
    for key in aDict.keys():
        if biggest["length"] < len(aDict[key]):
            biggest["name"] = key
            biggest["length"] = len(aDict[key])
    return biggest
