# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:36:56 2019

@author: Ismail Bourbie
"""

def printMove(fr, to):
    print("move from: " + str(fr) + " to " + str(to))
    
def towers(disc, fr, to, spare):
    if disc == 1:
        printMove(fr, to)
    else:
        towers(disc-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(disc-1, spare, to, fr)


towers(4, "P1", "P2", "p3")