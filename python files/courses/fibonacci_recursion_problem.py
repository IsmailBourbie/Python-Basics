# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:29:12 2019

@author: Ismail Bourbie
"""

def fib(x):
    global numbFuncCall
    numbFuncCall += 1
    if x == 1 or x == 0:
        return 1
    elif x == 2:
        return 2
    else:
        return fib(x - 1) + fib(x - 2)



## efficient algo using dictionary

def fib_efficent(n, d):
    global numbFuncCall
    numbFuncCall += 1
    if n in d:
        return d[n]
    ans = fib_efficent(n - 1, d) + fib_efficent(n - 2, d)
    d[n] = ans
    return ans

numbFuncCall = 0
print("fib:", fib(20), "number Func Call", numbFuncCall)
d = {1:1, 2:2}
numbFuncCall = 0
print("fib_efficent:", fib_efficent(20, d), "number Func Call", numbFuncCall)