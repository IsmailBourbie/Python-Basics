# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:36:08 2019

@author: Ismail Bourbie
"""

cube = 0.6
epsilon = 0.01
count_guesses = 0
is_negative = False
if cube < 0:
    is_negative = True
    cube = -cube
    
if (cube > 0 and cube < 1) or (cube < 0 and cube > -1):
    low = cube
    high = 1
else: 
    low = 1
    high = cube    
guess = (high + low) / 2

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
    count_guesses += 1

if is_negative:
    cube = -cube
    guess = -guess
print("num guesses:", count_guesses)
print(guess, "is the clost to the cube root of" , cube)