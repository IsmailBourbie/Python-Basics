# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:06:35 2019

@author: Ismail Bourbie
"""
input_num = int(input("Enter an integr number: "))
num = input_num
is_neg = False
if num < 0:
    is_neg = True
    num = abs(num)

result = ""
while num > 0:
    result = str(num%2) + result
    num = num//2

if is_neg:
    result = "-" + result

print("the binary representation of", input_num, "is: " + result)