# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:16:59 2019

@author: Ismail Bourbie
"""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
    print("Okay")
except ValueError:
    print("could not convert your input to number: ")
except ZeroDivisionError:
    print("Can't not devide by Zero")
except:
    print("Something wrong")